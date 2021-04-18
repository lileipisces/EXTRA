from datasketch import MinHash, LeanMinHash, MinHashLSH
import datetime
import pickle


sentence_path = 'sentences.pickle'  # resulting from process_sentence.py
directory = './'  # directory to save the grouped sentence ids
sim_thresholds = [0.9]  # the similarity between two near duplicates. To test more in this way [0.9, 0.85, 0.7]
shingle_size = 2  # preserve the word order to some extent
group_size = 5  # minimum number of sentences in a group


def now_time():
    """a string of current time"""
    return '[' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + ']: '


def get_k_shingles(raw_text, k=1):
    text_lower = raw_text.lower()
    words = text_lower.split()
    if k == 1:
        return set(words)

    shingles = []
    for start in range(len(words) + 1 - k):
        k_words = words[start:(start + k)]
        k_shingle = ' '.join(k_words)
        shingles.append(k_shingle)
    return set(shingles)


print(now_time() + 'Program running')
sentences = pickle.load(open(sentence_path, 'rb'))
minhash_dict = {}  # all sentences' MinHash
for idx, sentence in enumerate(sentences):
    if sentence['word_num'] < shingle_size:
        continue
    if sentence['subj_num'] > 0:
        continue
    if sentence['noun_num'] < 1:
        continue
    if sentence['adj_num'] < 1:
        continue

    exp = sentence['exp']
    shingle_set = get_k_shingles(exp, shingle_size)
    mh = MinHash()  # create MinHash for exp
    for s in shingle_set:
        mh.update(s.encode('utf8'))  # convert shingle s into MinHash
    minhash_dict[idx] = LeanMinHash(mh)
print(now_time() + 'Created Minhash')
del sentences  # to save memory


for sim_threshold in sim_thresholds:  # create MinHash for once, when testing multiple similarity values
    lsh = MinHashLSH(threshold=sim_threshold)  # create LSH index
    for idx, mh in minhash_dict.items():
        lsh.insert(str(idx), mh)
    print(now_time() + 'Created LSH for similarity {}'.format(sim_threshold))

    queried_ids = set()  # way more efficient than list
    exp_id_groups = []
    for idx, mh in minhash_dict.items():
        if idx in queried_ids:
            continue
        one_group_ids_str = lsh.query(mh)  # id list of one group of duplicate sentences
        for i in one_group_ids_str:
            lsh.remove(i)  # for efficiency
        one_group_ids_int = [int(i) for i in one_group_ids_str]
        if len(one_group_ids_int) > group_size:
            exp_id_groups.append(one_group_ids_int)  # only keep a group with enough sentences
        for i in one_group_ids_int:
            queried_ids.add(i)
    pickle.dump(exp_id_groups, open(directory + 'groups{}.pickle'.format(sim_threshold), 'wb'))
    print(now_time() + 'Saved a file for similarity {}'.format(sim_threshold))

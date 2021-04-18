import pickle
import nltk
import re


review_path = 'reviews.pickle'  # resulting from format_amazon.py
sentence_path = 'sentences.pickle'  # path to save sentences


def get_sentences(string):
    string = re.sub('[:,?!\n]', '.', string)
    sentences = [sent.strip() for sent in string.split('.') if sent.strip() != '']
    return sentences


def get_sentence_attr(string):
    subj_num = 0
    noun_num = 0
    adj_num = 0
    words = string.lower().split()
    w_t_list = nltk.pos_tag(words)
    for (w, t) in w_t_list:
        if w in subj_words:
            subj_num += 1
        if t in noun_taggers:
            noun_num += 1
        if t in adj_taggers:
            adj_num += 1
    return len(words), subj_num, noun_num, adj_num


subj_words = ['i', 'me', 'my', 'mine', 'myself', 'we', 'us', 'our', 'ours', 'ourselves']
noun_taggers = ['NN', 'NNP', 'NNPS', 'NNS']
adj_taggers = ['JJ', 'JJR', 'JJS']


reviews = pickle.load(open(review_path, 'rb'))
sentences = []
for idx, review in enumerate(reviews):
    text = review['text']
    exps = get_sentences(text)
    for exp in exps:
        word_n, subj_n, noun_n, adj_n = get_sentence_attr(exp)
        sentence = {
            'review_idx': idx,
            'exp': exp,
            'word_num': word_n,
            'subj_num': subj_n,
            'noun_num': noun_n,
            'adj_num': adj_n,
        }
        sentences.append(sentence)
pickle.dump(sentences, open(sentence_path, 'wb'))

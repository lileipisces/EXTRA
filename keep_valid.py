import pickle
import json


review_path = 'reviews.pickle'  # resulting from format_amazon.py
sentence_path = 'sentences.pickle'  # resulting from process_sentence.py
group_path = 'groups0.9.pickle'  # resulting from group_sentence.py
ID_path = 'IDs.pickle'  # path to save explanation IDs
id2exp_path = 'id2exp.json'  # path to save id2exp


reviews = pickle.load(open(review_path, 'rb'))
sentences = pickle.load(open(sentence_path, 'rb'))
exp_id_groups = pickle.load(open(group_path, 'rb'))
id2doc = {}
for group in exp_id_groups:
    exp_idx = list(group)[0]  # keep one explanation in each group
    for oexp_idx in group:
        sentence = sentences[oexp_idx]
        review_idx = sentence['review_idx']
        if review_idx not in id2doc:
            review = reviews[review_idx]
            json_doc = {
                'user': review['user'],
                'item': review['item'],
                'rating': review['rating'],
                'time': review['time'],
                'exp_idx': [str(exp_idx)],
                'oexp_idx': [str(oexp_idx)]
            }
            id2doc[review_idx] = json_doc
        else:
            id2doc[review_idx]['exp_idx'].append(str(exp_idx))
            id2doc[review_idx]['oexp_idx'].append(str(oexp_idx))


IDs = []
idx_set = set()
for _, doc in id2doc.items():
    IDs.append(doc)
    exp_idx = doc['exp_idx']
    oexp_idx = doc['oexp_idx']
    idx_set |= set(exp_idx) | set(oexp_idx)
pickle.dump(IDs, open(ID_path, 'wb'))


id2exp = {}
for idx, sentence in enumerate(sentences):
    idx = str(idx)
    if idx in idx_set:
        id2exp[idx] = sentence['exp']
with open(id2exp_path, 'w', encoding='utf-8') as f:
    json.dump(id2exp, f, indent=4)

import pickle
import json


ID_path = 'IDs.pickle'  # resulting from keep_valid.py
id2exp_path = 'id2exp.json'  # resulting from keep_valid.py
sample_idx = [100, 9999, 100000]  # take some samples to look at


IDs = pickle.load(open(ID_path, 'rb'))
with open(id2exp_path, 'r', encoding='utf-8') as f:
    id2exp = json.load(f)
for s_idx in sample_idx:
    record = IDs[s_idx]
    exp_idx = record['exp_idx']
    oexp_idx = record['oexp_idx']
    print('record {}'.format(s_idx))
    for oi, ei in zip(oexp_idx, exp_idx):
        print('original explanation {}: {}'.format(oi, id2exp[oi]))
        print('grouped explanation {}: {}'.format(ei, id2exp[ei]))

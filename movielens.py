from datetime import datetime
import pickle
import json


ID_path = 'IDs.pickle'  # resulting from keep_valid.py
id2exp_path = 'id2exp.json'  # resulting from keep_valid.py
ID_txt_path = 'IDs.txt'  # path to save explanation IDs in plain text
id2exp_txt_path = 'id2exp.txt'  # path to save id2exp in plain text


IDs = pickle.load(open(ID_path, 'rb'))
lines = []
for record in IDs:
    # userID::itemID::rating::timestamp::expID:expID::oexpID:oexpID
    user = record['user']
    item = record['item']
    rating = record['rating']
    time = int(datetime.strptime(record['time'], '%Y-%m-%d').timestamp())
    exp_idx = record['exp_idx']
    oexp_idx = record['oexp_idx']
    exp = ':'.join(exp_idx)
    oexp = ':'.join(oexp_idx)
    line = '::'.join([user, item, str(rating), str(time), exp, oexp])
    lines.append(line)
with open(ID_txt_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))


with open(id2exp_path, 'r', encoding='utf-8') as f:
    id2exp = json.load(f)
lines = []
for (idx, exp) in id2exp.items():
    # expID::exp
    line = '::'.join([idx, exp])
    lines.append(line)
with open(id2exp_txt_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

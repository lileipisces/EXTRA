ID_txt_path = 'IDs.txt'  # resulting from movielens.py
id2exp_txt_path = 'id2exp.txt'  # resulting from movielens.py

with open(ID_txt_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        [user, item, rating, timestamp, expIDs, oexpIDs] = line.split('::')
        exp_idx = expIDs.split(':')  # a list
        oexp_idx = oexpIDs.split(':')  # a list
        print('a record:')
        print('user: {}'.format(user))
        print('item: {}'.format(item))
        print('rating: {}'.format(rating))
        print('timestamp: {}'.format(timestamp))
        for oi, ei in zip(oexp_idx, exp_idx):
            print('original explanation: {}'.format(oi))
            print('grouped explanation: {}'.format(ei))
        break  # only display the first record

with open(id2exp_txt_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        [idx, exp] = line.split('::')
        print('explanation {}: {}'.format(idx, exp))
        break  # only display the first record

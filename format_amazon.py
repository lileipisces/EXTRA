from datetime import datetime
import pickle
import gzip


raw_path = 'reviews_Movies_and_TV_5.json.gz'  # path to load raw reviews
review_path = 'reviews.pickle'  # path to save reviews

reviews = []
for line in gzip.open(raw_path, 'r'):
    review = eval(line)
    text = ''
    if 'summary' in review:
        summary = review['summary']
        if summary != '':
            text += summary + '\n'
    text += review['reviewText']

    json_doc = {'user': review['reviewerID'],
                'item': review['asin'],
                'rating': int(review['overall']),
                'text': text,
                'time': datetime.fromtimestamp(int(review['unixReviewTime'])).strftime('%Y-%m-%d')}
    reviews.append(json_doc)
pickle.dump(reviews, open(review_path, 'wb'))

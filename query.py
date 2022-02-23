import pickle
import os


FILENAME = f'./store/reviews.pkl'


def query_test_reviews(client):
    reviews = []
    if os.path.isfile(FILENAME):
        reviews = _load_reviews()
    else:
        for review in client.find({}):
            reviews.append(
                {
                    'review': review['review_text'],
                    'id': review['review_id'],
                    'book_id': review['book']['book_id'],
                    'review_count': review['book']['text_reviews_count']
                })
        _save_reviews(reviews)
    return reviews


def _save_reviews(reviews):
    with open(FILENAME, 'wb') as output:
        pickle.dump(reviews, output, pickle.HIGHEST_PROTOCOL)
    print('Saved.')


def _load_reviews():
    with open(FILENAME, 'rb') as input:
        reviews = pickle.load(input)
    print('Loaded.')
    return reviews

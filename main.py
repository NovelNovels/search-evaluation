from evaluation import Evaluation
from connection import connect_mongodb
from query import query_test_reviews


def main():
    print('Connecting to MongoDB...')
    client = connect_mongodb()

    print('Querying all reviews from the test collection...')
    reviews = query_test_reviews(client)
    print('Done querying.')

    eval = Evaluation(reviews)

    test_corpus = ['fantasy', 'scary', 'twist', 'excited', 'boring']
    print('Start evaluating...')
    for phrase in test_corpus:
        print(eval.run(phrase))
    print('Done.')


if __name__ == '__main__':
    main()

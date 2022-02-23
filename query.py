def query_test_reviews(client):
    reviews = []
    for review in client.find({}):
        reviews.append(
            {'review': review['review_text'], 'id': review['review_id'], 'book_id': review['book']['book_id']})
    return reviews

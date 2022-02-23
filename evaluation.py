import collections
import numpy as np
import requests


class Evaluation():
    def __init__(self, reviews):
        self.reviews = reviews

    def raw_query(self, phrase):
        query = []
        count = collections.defaultdict(int)
        for r in self.reviews:
            if phrase in r['review']:
                # count[r['book_id']] += 1
                count[r['book_id']
                      ] += r['review'].count(phrase) / len(r['review'])
                query.append(
                    (r['id'], r['review'], r['review'].count(phrase), r['book_id']))
        ranked = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return query, ranked, count

    def api_query(self, phrase):
        response = requests.get(
            f'https://booksearch-fastapi.nw.r.appspot.com/search?q={phrase}')
        results = response.json()['results']
        books = []
        for book in results:
            books.append(book['book_id'])
        return books

    def cal_ndcg(self, ideal, normal):
        dcg = normal[0]
        idcg = ideal[0]
        for i in range(1, len(ideal)):
            dcg += normal[i] / np.log2(i + 1)
            idcg += ideal[i] / np.log2(i + 1)
        return dcg / idcg

    def run(self, phrase):
        _, ranked, count = self.raw_query(phrase)
        books = self.api_query(phrase)
        i_book_ids, i_book_scores = zip(*ranked)
        _, book_scores = zip(*[(b, count[b]) for b in books])

        found = 0
        for b in books:
            if b in i_book_ids:
                found += 1

        ndcg = self.cal_ndcg(i_book_scores[:len(book_scores)], book_scores)

        return found / len(books), ndcg

import unittest

import article_processor as processor


class TestLineParsing(unittest.TestCase):

    def test_processor_marks_articles_that_has_empty_author(self):
        article = {'author': '', 'content': 'content body', 'rating': 1, 'errors': []}
        article2 = {'author': 'Muhammad', 'content': 'content body', 'rating': 1, 'errors': []}
        articles = [article, article2]

        for a in articles:
            processor.inspect_empty_author(a)
        self.assertIn('No_Author', articles[0]['errors'])


if __name__ == '__main__':
    unittest.main()

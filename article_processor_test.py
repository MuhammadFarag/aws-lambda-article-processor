import unittest

import article_processor as processor


class TestLineParsing(unittest.TestCase):
    article = {'author': '', 'content': 'content body', 'rating': 1, 'errors': []}
    article2 = {'author': 'Muhammad', 'content': 'content body', 'rating': 1, 'errors': []}

    def test_processor_marks_articles_that_has_empty_author(self):
        self.assertIn('No_Author', processor.inspect_empty_author(self.article)['errors'])


if __name__ == '__main__':
    unittest.main()

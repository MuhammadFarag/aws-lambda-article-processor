import unittest

import article_processor as processor


class TestLineParsing(unittest.TestCase):

    def test_processor_marks_articles_that_has_empty_author(self):
        article = {'author': '', 'content': 'content body', 'rating': 1, 'errors': []}
        self.assertIn('No_Author', processor.inspect_empty_author(article)['errors'])

    def test_processor_will_not_mark_articles_that_has_no_empty_author(self):
        article = {'author': 'Muhammad', 'content': 'content body', 'rating': 1, 'errors': []}
        self.assertFalse(processor.inspect_empty_author(article)['errors'], 'No errors should be found in errors list')

    def test_processor_will_count_the_number_of_words_in_the_content(self):
        article = {'author': '', 'content': 'content body', 'rating': 1, 'errors': []}
        self.assertEqual(2, processor.content_length(article))


if __name__ == '__main__':
    unittest.main()

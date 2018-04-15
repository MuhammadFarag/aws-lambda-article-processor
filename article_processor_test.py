import unittest

import article_processor as processor


class TestLineParsing(unittest.TestCase):

    def test_processor_marks_articles_that_has_empty_author(self):
        article = {"author": "", "content": "content body", "rating": 1, "errors": []}
        self.assertIn("No_Author", processor.inspect_empty_author(article, None)["errors"])

    def test_processor_will_not_mark_articles_that_has_no_empty_author(self):
        article = {"author": "Muhammad", "content": "content body", "rating": 1, "errors": []}
        self.assertFalse(processor.inspect_empty_author(article, None)["errors"], "No errors should be found in errors list")

    def test_processor_will_count_the_number_of_words_in_the_content(self):
        article = {"author": "", "content": "content body", "rating": 1, "errors": []}
        self.assertEqual(2, processor.content_length(article, None)['length'])

    def test_processor_adds_five_to_the_value_of_rating(self):
        article = {"author": "", "content": "content body", "rating": 1, "errors": []}
        self.assertEqual(6, processor.pump_rating(article, None)['rating'])

    def test_processor_capitalizes_author_name(self):
        article = {"author": "author name", "content": "content body", "rating": 1, "errors": []}
        self.assertEqual('Author Name', processor.capitalize_author_name(article, None)['author'])

    def test_naive_merge_capitalized_author_and_pumped_rating(self):
        capitalized = {"author": "Author Name", "content": "content body", "rating": 1, "errors": []}
        pumpedRating = {"author": "author name", "content": "content body", "rating": 6, "errors": []}
        expected = {"author": "Author Name", "content": "content body", "rating": 6, "errors": []}
        self.assertEqual(expected, processor.naive_merge_capitalized_author_and_pumped_rating([capitalized, pumpedRating], None))

    def test_naive_merge_capitalized_author_and_pumped_rating_reversed_input_list(self):
        capitalized = {"author": "Author Name", "content": "content body", "rating": 1, "errors": []}
        pumpedRating = {"author": "author name", "content": "content body", "rating": 6, "errors": []}
        expected = {"author": "Author Name", "content": "content body", "rating": 6, "errors": []}
        self.assertEqual(expected, processor.naive_merge_capitalized_author_and_pumped_rating([pumpedRating, capitalized], None))

if __name__ == '__main__':
    unittest.main()

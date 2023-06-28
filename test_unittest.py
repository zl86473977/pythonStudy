import unittest
from util import my_adder, Sentence


class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5, 3), 8)

    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5, 3), -2)

    def test_negative_with_negative(self):
        self.assertEqual(my_adder(-5, -1), -6)

    def test_true(self):
        # AssertionError: False is not true
        self.assertTrue(2 not in [1, 3 - 1])

    def test_notIn(self):
        # AssertionError: 2 unexpectedly found in [1, 2]
        self.assertNotIn(2, [1, 3 - 1])

# assertTrue(a) --- assert a is True
# assertIn(a, b) --- assert a in b
# assertNotEqual(a, b) --- assert a != b
# assertFalse(a) --- assert a is False
# assertNotIn(a, b) --- assert a not in b


class TestSentence(unittest.TestCase):
    def setUp(self) -> None:
        self.sentence = Sentence("Hello world!")

    def test_letter_count(self):
        self.assertEqual(self.sentence.letter_count(), 12)

    def test_word_count(self):
        self.assertEqual(self.sentence.word_count(), 2)

    def test_upper(self):
        self.assertEqual(self.sentence.upper(), "HELLO WORLD!")

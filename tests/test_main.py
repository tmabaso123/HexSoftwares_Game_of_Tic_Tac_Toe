import unittest
from unittest.mock import patch
from game import hangman  


class TestHangman(unittest.TestCase):

    def test_read_file(self):
        with patch("builtins.open", unittest.mock.mock_open(read_data="fruit\nbeach\nsweet")):
            words = hangman.read_file("words.txt")
            self.assertEqual(words, ["fruit\n", "beach\n", "sweet"])

    def test_select_random_word_from_words(self):
        words = ["fruit", "beach", "sweet"]
        with patch("random.choice", return_value="beach"):
            word = hangman.select_random_word_from_words(words)
            self.assertEqual(word, "beach")

    def test_get_index_of_guess(self):
        word = "fruit"
        index = hangman.get_index_of_guess("u", word)
        self.assertEqual(index, 2)  

    def test_get_index_of_guess_not_found(self):
        word = "fruit"
        index = hangman.get_index_of_guess("z", word)
        self.assertEqual(index, len(word))  
    def test_display_hangman(self):
        hangman_stage_0 = """
 +---+
 |   |    
 0   |
/|\\  |
/ \\  |
     |
======
    """
        self.assertEqual(hangman.display_hangman(0).strip(), hangman_stage_0.strip())

    def test_display_word_progress(self):
        word_progress = ["_", "_", "u", "i", "_"]
        with patch("builtins.print") as mocked_print:
            hangman.display_word_progress(word_progress)
            mocked_print.assert_has_calls([
                unittest.mock.call("_", end=" "),
                unittest.mock.call("_", end=" "),
                unittest.mock.call("u", end=" "),
                unittest.mock.call("i", end=" "),
                unittest.mock.call("_", end=" "),
                unittest.mock.call()  
            ])


if __name__ == "__main__":
    unittest.main()

import unittest
from translator import english_to_french, french_to_english
class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertNotEqual(english_to_french("Bye"), "Bonjour") 

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("Bonjour"), "Hello") 
        self.assertEqual(french_to_english("Bonjour"), "Hi") 
        self.assertEqual(french_to_english("Au revoir"), "Good bye") 

if __name__ == '__main__':
    unittest.main()
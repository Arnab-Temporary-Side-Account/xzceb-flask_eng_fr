import unittest

from translator import english_to_french, french_to_english
class TestFTE(unittest.TestCase): 
    def test1(self):  #Test for null input
        self.assertEqual(french_to_english(""), "")  
    def test2(self):    
        self.assertEqual(french_to_english("Bonjour"), "Hello") 
    def test3(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

class TestETF(unittest.TestCase): 
    def test1(self):  #Test for null input
        self.assertEqual(english_to_french(""),"")
    def test2(self):  
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test3(self):   
        self.assertNotEqual(english_to_french("Hello"), "Hello")


unittest.main()
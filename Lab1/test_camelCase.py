"""
Dan Smestad ITEC 2905-80 Capstone 2/2/2021.
Python testing example for testing your code. 
Start your test functions with the word test!
don't forget assert mothods. Team testing is good!

testing python_camelCase program
"""
import python_camelCase  #my camelcase preogram
from unittest import TestCase  #import modules

class TestCamelCase(TestCase):  #class declartion

    def test_camelCase_sentence(self):
        self.assertEqual('helloWorld', python_camelCase.camelCase('HELLO WORLD'))
        # testing sentence build that matches.

    def test_camelCase_sentence_with_space(self):
        self.assertEqual('', python_camelCase.camelCase(''))  #I typed this one too
    
    def test_camelCase_sentence_with_emojie(self):
        self.assertEqual('👽🌎🌺🐑🌳', python_camelCase.camelCase('👽🌎🌺🐑🌳'))  
        #copy pasted this in emoji, there isnt another way to place them?.



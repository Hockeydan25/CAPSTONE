"""
Dan Smestad ITEC 2905-80 Capstone 2/13/2021.
Python Lab4. 
Python testing example for testing your code. 
Start your test functions with the word test!
don't forget assert mothods. Team testing is good!

testing camel_case program
"""
import camel_case  # file imported for testing program.
from unittest import TestCase  # import modules for testcase 

class TestCamelCase(TestCase):  #class declartion

    def test_camelCase_sentence(self):
        self.assertEqual('helloWorld', camel_case.camelcase('HELLO WORLD'))
        # testing sentence build that matches.

    def test_camelCase_sentence_with_space(self):
        self.assertEqual('', camel_case.camelcase(''))  #I typed this one too
        # testing basic spacing could have much more testing for differnet spacing.

    def test_camel_case_many_words(self):

        input_and_expected_outputs = {
            'two words': 'twoWords',
            'this is a sentence': 'thisIsASentence',
            'Here is a long sentence with many words' : 'hereIsALongSentenceWithManyWords',
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel_case.camelcase(input_val))
            #  many words and seniros. Variable name is really good here.

    def test_camelCase_sentence_with_emojie(self):
        input_and_expected_outputs = {
        'π½ π½ππΊπ': 'π½π½ππΊπ',
        'π½ ππΊππ³ π΅π¬': 'π½ππΊππ³π΅π¬',

        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel_case.camelcase(input_val))
        #had to fins and copy paste these emojis in, there is another way to place them?
        # code sample from claraj.


    def test_camelCase_special_characters(self):
        input_and_expected_outputs = {
        'def@_!#$%^&*()<>?/\|}{~:;[] ear': 'defEar', 
        '@_!#$%^&*()<>?/\|}{~:;[]def ear': 'defEar',
        '@_!#$%^&*()<>?/\|}{~:;[]def ear': 'defEar',
        'def ear@_!#$%^&*()<>?/\|}{~:;[]': 'defEar',

        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel_case.camelcase(input_val))
        # code sample from claraj.
        # testing sentence build that matches any special charters.    
        #Optional: implement a filter to remove special characters from the 
        # input string. Write a test for this filter. 

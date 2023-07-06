'''Translate using MyMemoryTranslator.'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''Translate from English to French.'''
    #write the code here
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Translate from French to English.'''
    #write the code here
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text

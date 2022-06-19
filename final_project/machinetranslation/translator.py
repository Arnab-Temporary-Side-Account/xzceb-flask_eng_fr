import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    This function translates from English to French
    '''
    if english_text=='':
        return ''

    french_translation = language_translator.translate(text=english_text,model_id='en-fr')
    french_translation =  french_translation.get_result()
    french_text = french_translation["translations"][0]
    french_text=french_text["translation"]
    return french_text

def french_to_english(french_text):
    '''
    This function translates from French to English
    '''
    if french_text=='':
        return ''
    english_translation = language_translator.translate(text=french_text,model_id='fr-en')
    english_translation=english_translation.get_result()
    english_text = english_translation["translations"][0]
    english_text=english_text["translation"]
    return english_text

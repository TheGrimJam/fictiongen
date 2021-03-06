# Book related functions
from core import development_tools  as log
import os
import codecs 
import markovify
from django.core.files import File
from django.core.files.base import ContentFile
from django.apps import apps
from markov_functions.text_processors import mk_nltk

## These should maybe be part of models.py
def build_model(text, config):
  if config['pos_enabled']:
    return (mk_nltk.POSifiedText(text, state_size=config['state_size']))
  else:
    return (markovify.Text(text, state_size=config['state_size']))

def get_book_model(bookID, config):
  try:
    Book = apps.get_model('markov_functions', 'Book') # Lazy model import to avoid circularity.
    book = Book.objects.get(pk=bookID) 
    prebuilt_model = "" # book.model.read()
    # Need to fix prebuild model to use the below.
    if prebuilt_model != "":
      model = prebuilt_model
    else:
      contents = book.file.read().decode('utf-8','ignore')
      model = build_model(contents, config)
    return model
  except:
    log.exception()
    return "Failed"
 
def load_active_books(config):
  text = ""
  combined_models = build_model("Sally was a lumpkin", config) # Initialise a blank text object to combine with
  print(combined_models)
  for book,weight in config['book_ids'].items():
    book_model = get_book_model(int(book), config)
    combined_models = markovify.combine([combined_models, book_model],[ 1 , int(weight) ]) # Combine total model with current loop model with it's prescribed weight.
  return combined_models



def save_book_models(self, state_range=[2,5]):
  """ Takes a file object, creates several models and stores them alongside the original """
  generated_model = build_model(self.file.read().decode('UTF-8'), 2)# add in loop for # of ranges
  filename = self.file.name + "_model_2.txt"
  json_model = generated_model.to_json()
  return filename, ContentFile(json_model)
  return filename, json_model
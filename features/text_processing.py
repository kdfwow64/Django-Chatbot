import numpy as np
import re
from random import choice

def remove_no_need(words, no_need):
    """takes in a received message, and removes any word found in no_need"""
    eek = unigram(words)
    white_weirdo = []
    for i in eek:
        if i not in no_need:
            white_weirdo.append(i)
    return white_weirdo

def check_inside(l, rm_list):
  """for each item in list l, it checks if the item is in the received_message's list"""
  return len(get_partial_match(rm_list, l)) != 0

def autocorrect(given_word, some_list):
  """takes in a word and some_list, and returns the lowercase of the most
     matching word from some_list up to a distance of 4"""
  print("====START MY AUTOCORRECT!====")
  given_word = given_word.lower()
  save = {}
  some_list = list(filter(lambda word: abs(len(word) - len(given_word)) < 4, some_list))
  some_list = list(map(str.lower, some_list))
  if len(some_list) == 0:
    return given_word
  match = some_list[0]
  for word in some_list:
    if word not in save:
        save[word] = levenshtein(word, given_word)
    if save[word] == 0:
        return word
    if save[word] < save[match]:
      print(given_word, "sounds like", word)
      match = word
  if save[match] < 4:
    return match
  else:
    return given_word

def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)
    if len(target) == 0:
        return len(source)
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    previous_row = np.arange(target.size + 1)
    for s in source:
        current_row = previous_row + 1
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)
        previous_row = current_row
    return previous_row[-1]

def unigram(s):
  return re.sub(r'([^\s\w]|_)+', '', s).lower().split()

def ngram(n, l):
  out = []
  for i in range(len(l)-n+1):
    temp_string = " ".join(l[i:i+n])
    out.append(temp_string)
  return out

def get_partial_match(wl, l2m):
  """take in a list of strings, and another list called l2m,
  and returns the list of strings in l2m that are found in wl."""
  n = len(wl)
  match_list = []
  for C in range(n, 0, -1):
    grams = ngram(C, wl)
    for i in l2m:
      if i in grams:
        match_list.append(i)
  return match_list

def get_full_match(wl, l2m):
  """takes in a list(of strings), and another list called l2m,
  and if something from l2m is in list, then we return True or False if list matches l2m exactly"""
  n = len(wl)
  output = []
  for C in range(n, 0, -1):
    grams = ngram(C, wl)
    for i in l2m:
      if i in grams:
        output.append(i)
  return output == l2m

def contains_key(text, tuples):
  for tup in tuples:
    if type(tup) == str:
      tup = (tup, )
    tup = tuple(map(str.lower, tup))
    if contains_every_key(text, tup):
      return True
  return False

def contains_every_key(text, tup):
  find_strings = map(lambda s: contains_string(text, s), tup)
  return False not in find_strings

def contains_string(text, string):
  length = len(string.split())
  return string in ngram(length, unigram(text))

def punk_handler(s):
   y = ""
   for i in s.lower():
     if i.isalnum() or i == " ":
       y += i
     elif i == "," or i == "\n":
       y += " "
   return y

def split_sentence_by_list_of_words(s, w):
   s = punk_handler(s)
   s = "  " + s + "  "
   for i in w:
       s = s.replace(" "+i+" ", "  ")
   result = []
   for i in s.split("  "):
     if not i == "":
       result.append(i.strip())
   return result

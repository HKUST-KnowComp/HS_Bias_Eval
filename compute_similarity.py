import re
import os
import numpy as np
from utils import *
from constants import   *
import fastText_multilingual
from fastText_multilingual import fasttext
from fastText_multilingual.fasttext import FastVector

def get_sim1_fasttext(dictionary, list1, list2): 
  score = 0.0
  final_score = 0.0
  similarity = 0.0
  for word1 in list1:
    for word2 in list2:
        if word1 == word2:
            similarity=1.0
        else:
            if word1 in dictionary:
                w1_vector = dictionary[word1]
                if word2 in dictionary:
                    w2_vector = dictionary[word2]
                    similarity = FastVector.cosine_similarity(w1_vector, w2_vector)
        score+=similarity
        final_score += score/float(len(list2))
        score = 0.0
  return final_score/float(len(list1))

def get_sim2_fasttext(dictionary, list1, list2):
  score = 0.0
  similarity =  0.0
  final_score = 0.0
  for word1 in list1:
    for word2 in list2:
      if word1 == word2:
        similarity = 1.0
        score = similarity
      elif word1 in dictionary:
        w1_vector = dictionary[word1]
        if word2 in dictionary:
          w2_vector = dictionary[word2]
          similarity = FastVector.cosine_similarity(w1_vector, w2_vector)
          if similarity>score:
            score=similarity
    final_score += score
    score = 0.0
  return final_score/float(len(list1))

def get_b1_fasttext(topics_dict, keywords, embed_path):
    dictionary = upload_fasttext_embeddings(embed_path)
    result = 0.0
    sum_res = 0.0
    for key1, topics_list1 in topics_dict.items():
        result = get_sim1_fasttext(dictionary, topics_list1, keywords)
        sum_res += result
    print('Final score: ')
    print (sum_res/float(len(topics_dict)))
    return sum_res/float(len(topics_dict))

def get_b2_fasttext(topics_dict, keywords, embed_path):
    dictionary = upload_fasttext_embeddings(embed_path)
    result = 0.0
    sum_res = 0.0
    for key1, topics_list1 in topics_dict.items():
        result = get_sim2_fasttext(dictionary, topics_list1, keywords)
        sum_res += result
    print('Final score: ')
    print (sum_res/float(len(topics_dict)))

import pandas as pd 
import csv
import gensim
from constants import *
from utils import preprocess
import numpy as np
import nltk
from gensim import corpora, models
from matplotlib import pyplot
import math
from collections import Counter
from gensim.models import Word2Vec


def run_topic_models(file_path, number_topics, language):
    data = pd.DataFrame()
    docs = []
    if(file_path.endswith('.tsv')):
        data = pd.read_csv(file_path, delimiter='\t')
    else:
        data = pd.read_csv(file_path)
    # You can preprocess your data beforehand, using preprocess
    for idx, row in data.iterrows():
        doc = preprocess(row['tweet'], language)
        docs.append(doc)
    vocab = set(x for doc in docs for x in doc)
    dictionary = gensim.corpora.Dictionary(docs)
    bow_corpus = [dictionary.doc2bow(doc) for doc in docs]
    lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=number_topics, id2word=dictionary, passes=2, workers=2)
    return lda_model

def process_topics(filename, number_words, number_topics, language): 
    topics  = {}
    replace_by_blank_symbols=re.compile('\"|\*|\.|[0-9]+| ')    
    i = 0
    new_list = []
    for idx, topic in run_topic_models(filename, number_topics, language).print_topics(number_topics, number_words):
        list_elements = topic.split('+')
        for element in list_elements:
            element = replace_by_blank_symbols.sub('', element)
            new_list.append(element)
        topics[i]=new_list
        new_list = []
        i+=1
    #print(topics)
    return topics

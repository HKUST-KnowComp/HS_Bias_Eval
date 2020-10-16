from constants import *
from utils import *
from run_topic_models import *
from compute_similarity import *
from run_topic_models import *


def compute_b1(dataset, language, similarity_metric, topic_number, word_number, embed_path):
    topics_dict =process_topics(dataset, topic_number, word_number, language)
    if similarity_metric == 'fasttext':
        return get_b1_fasttext(topics_dict, KEYWORDS_LANGUAGE[language], embed_path) 
    
def compute_b2(dataset, language, similarity_metric,  topic_number, word_number, embed_path):
    topics_dict = process_topics(dataset, topic_number, word_number, language)
    if similarity_metric == 'fasttext':
        return get_b2_fasttext(topics_dict, KEYWORDS_LANGUAGE[language], embed_path) 
   

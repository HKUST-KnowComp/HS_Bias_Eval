import argparse
import os
import random
import sys
import numpy as np
from constants import LANGUAGES, LANGUAGE_CODE, SIMILARITY_MEASURES, BIAS_METRICS
from bias_metrics import compute_b1, compute_b2
from utils import * #process_topics_with_number_words


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run Bias Metrics',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--language', required=True, choices=LANGUAGES, #if you want to run on other languages, you should add it to the constant array LANGUAGES, its language code to LANGUAGE_CODE and download its fasttext embeddings
                      help='the language of the dataset to be evaluated')
    parser.add_argument('--dataset', type=str, required=True,
                        help='the path to the dataset that needs to be evaluated')
    parser.add_argument('--similarity_measure', default='fasttext', choices=SIMILARITY_MEASURES,
                        help='the the similarity measure that will be used during evaluation')
    parser.add_argument('--metric', type = str, default='b1', choices=BIAS_METRICS,
                        help='Would you like to compute B1 or B2? Default = B1.')
    parser.add_argument('--embeds_path', type=str, required=True,
                        help='path to the embeddings file. if you are using Babylon, please download the required embeddings from https://github.com/babylonhealth/fastText_multilingual.')
    parser.add_argument('--topic_number', type=int, default=8,
                        help='the number of topics you are evaluating bias on.')
    parser.add_argument('--word_number', type=int, default=8,
                        help='the number of words you are evaluating bias on.')
    
    args = parser.parse_args()
    if args.dataset.endswith(os.sep):
        args.dataset = args.dataset[:-1]
    if args.embeds_path.endswith(os.sep):
        args.dataset = args.dataset[:-1]
    language = args.language.lower()
    if args.metric == "b1":
        b1_score = compute_b1(args.dataset,language,args.similarity_measure, args.topic_number, args.word_number, args.embeds_path)
        print(b1_score)
    elif args.metric == "b2":
        b2_score = compute_b2(args.dataset,language,args.similarity_measure, args.topic_number, args.word_number, args.embeds_path)
        print(b2_score)

        

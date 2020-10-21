This is the code and data of our paper:
        
        @inproceedings{ousidhoum-etal-bias-eval-multilingual-hate-speech-2020,
    		   title = "Comparative Evaluation of Label-Agnostic Selection Bias in Multilingual Hate Speech Datasets",        
                       author = "Nedjma Ousidhoum,
            		         Yangqiu Song,
            		         Dit-Yan Yeung",
                       booktitle = "Proceedings of EMNLP",
                       year = "2020",
                       publisher =	"Association for Computational Linguistics",
	                   }
  

Description
----------
----------
This code uses topic models and semantic similarity to compute bias in hate speech datasets. 

You can preview our paper here: https://nedjmaou.github.io/nousidhoum_et_al_emnlp2020_hs_bias_eval.pdf

Requirements
-----------
-----------
Python 3.6

Gensim

Babylon embeddings for the tested language 

FastText multilingual

How to run the code
-------------------
-------------------
	python run_bias_metrics.py --language language_name --dataset /path/to/dataset.csv --metric b1 --embeds_path path/to/embeddings --topic_number x --word_number y

The dataset needs to be a CSV file that has 'tweet' as a column. We will update the code soon and will upload a full example.

Experiments
-----------
-----------

To replicate our experiments, please refer to the following datasets:

Arabic Data
-----------
1) Nuha Albadi, Maram Kurdi, and Shivakant Mishra. 2018. Are they our brothers? analysis and detection of religious hate speech in the arabic twittersphere. In Proceedings of ASONAM, pages 69–76. IEEE Computer Society.
[https://github.com/nuhaalbadi/Arabic_hatespeech]

2) Hala Mulki, Hatem Haddad, Chedi Bechikh Ali, and Halima Alshabani. 2019. L-HSAB: A Levantine twitter dataset for hate speech and abusive language. In Proceedings of the Third Workshop on Abusive Language Online, pages 111–118.
[https://github.com/Hala-Mulki/L-HSAB-First-Arabic-Levantine-HateSpeech-Dataset]

3) Nedjma Ousidhoum, Zizheng Lin, Hongming Zhang, Yangqiu Song, and Dit-Yan Yeung. 2019. Multilingual and multi-aspect hate speech analysis. In Proceedings of EMNLP-IJCNLP, pages 4675–4684
[https://github.com/HKUST-KnowComp/MLMA_hate_speech/]

English Data
------------
1) Antigoni-Maria Founta, Constantinos Djouvas, Despoina Chatzakou, Ilias Leontiadis, Jeremy Blackburn, Gianluca Stringhini, Athena Vakali, Michael Sirivianos, and Nicolas Kourtellis. 2018. Large scale crowdsourcing and characterization of twitter abusive behavior. In Proceedings of ICWSM, pages 491–500.
[https://github.com/ENCASEH2020/hatespeech-twitter]

2) Nedjma Ousidhoum, Zizheng Lin, Hongming Zhang, Yangqiu Song, and Dit-Yan Yeung. 2019. Multilingual and multi-aspect hate speech analysis. In Proceedings of EMNLP-IJCNLP, pages 4675–4684
[https://github.com/HKUST-KnowComp/MLMA_hate_speech/]

3) Zeerak Waseem and Dirk Hovy. 2016. Hateful symbols or hateful people? predictive features for hate speech detection on twitter. In Proceedings of the NAACL Student Research Workshop, pages 88–93.
[https://github.com/ZeerakW/hatespeech]


French Data
-----------
Nedjma Ousidhoum, Zizheng Lin, Hongming Zhang, Yangqiu Song, and Dit-Yan Yeung. 2019. Multilingual and multi-aspect hate speech analysis. In Proceedings of EMNLP-IJCNLP, pages 4675–4684
[https://github.com/HKUST-KnowComp/MLMA_hate_speech/]


German Data
-----------
Bjorn Ross, Michael Rist, Guillermo Carbonell, Benjamin Cabrera, Nils Kurowsky, and Michael Wojatzki. 2016. Measuring the Reliability of Hate Speech Annotations: The Case of the European Refugee Crisis. In Proceedings of NLP4CMC III: 3rd Workshop on Natural Language Processing for Computer-Mediated Communication, pages 6–9.
[https://github.com/UCSM-DUE/IWG_hatespeech_public]

Indonesian Data
---------------
Muhammad Okky Ibrohim and Indra Budi. 2019. Multi-label hate speech and abusive language detection in Indonesian twitter. In Proceedings of the Third Workshop on Abusive Language Online, pages 46–57.
[https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection]


Italian Data
------------
Manuela Sanguinetti, Fabio Poletto, Cristina Bosco, Viviana Patti, and Marco Stranisci. 2018. An italian twitter corpus of hate speech against immigrants. In Proceedings of LREC.
[https://github.com/msang/hate-speech-corpus]


Portuguese Data
---------------
Paula Fortuna, Joao Rocha da Silva, Juan Soler Company, Leo Wanner, and Sergio Nunes. 2019. A hierarchically-labeled portuguese hate speech dataset. In Proceedings of the 3rd Workshop on Abusive Language Online (ALW3).
https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset]

from __future__ import division
import string
import nltk
from collections import Counter
import os
import json

import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from scipy.cluster.vq import whiten


import statistics
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
word_tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

class Pacling:
    def __init__(self):
        pass

    def classify(self, author_string, test_string):
        pa = Counter(nltk.bigrams(author_string))
        pt = Counter(nltk.bigrams(test_string))

        total = 0

        worst_possible = 0
        for b in pa:
            f1 = pa[b] / len(author_string)  # I think this will normalize fine
            f2 = pt[b] / len(test_string)
            try:
                total += (2 * (f1 - f2) / (f1 + f2))**2
                worst_possible += (2 * (f1 + f2) / (f1 + f2))**2
            except ZeroDivisionError:
                pass
        return abs(1 - (total / worst_possible))


        for key in set(pa.keys() + pt.keys()):
            f1 = pa[key]
            f2 = pt[key]
            total += (2 * (f1 - f2) / (f1 + f2)) ** 2
        return total

pacling = Pacling()

def lexical_stuff(comments):
        # print pacling.classify('\n'.join(sahil), '\n'.join(sahil))
        comments = filter(lambda k: k != "", comments)

        fvs_lexical = np.zeros((len(comments), 3), np.float64)
        fvs_punct = np.zeros((len(comments), 3), np.float64)
        for e, ch_text in enumerate(comments):
            tokens = nltk.word_tokenize(ch_text.lower())
            words = word_tokenizer.tokenize(ch_text.lower())
            sentences = sentence_tokenizer.tokenize(ch_text)
            vocab = set(words)
            words_per_sentence = np.array([len(word_tokenizer.tokenize(s)) for s in sentences])

            fvs_lexical[e, 0] = words_per_sentence.mean()
            fvs_lexical[e, 1] = words_per_sentence.std()
            if words:
                fvs_lexical[e, 2] = len(vocab) / float(len(words))
            if sentences:
                fvs_punct[e, 0] = tokens.count(',') / float(len(sentences))
                fvs_punct[e, 1] = tokens.count(';') / float(len(sentences))
                fvs_punct[e, 2] = tokens.count(':') / float(len(sentences))
    
        # apply whitening to decorrelate the features
        fvs_lexical = whiten(fvs_lexical)
        fvs_punct = whiten(fvs_punct)

        return np.nan_to_num(fvs_lexical), np.nan_to_num(fvs_punct)

        # # average number of words per sentence
        # words_per_sentence_avg = sum(words_per_sentence) / float(len(words_per_sentence))
        # words_per_sentence_deviation = statistics.stdev(words_per_sentence)
        # lexical_diversity = len(vocab) / float(len(words))

        # comma_punct = tokens.count(',') / float(len(sentences))
        # semi_colon_punct = tokens.count(';') / float(len(sentences))
        # colon_punct = tokens.count(':') / float(len(sentences))

def predict_authors(fvs):
    km = KMeans(n_clusters=2, init='k-means++', n_init=10, verbose=0)
    km.fit(fvs)
    return km

with open('./data/vrckid.data', 'r') as f, open('./data/dick-nipples.data', 'r') as f2:
    sahil = f.read()
    elaus = f2.read()
    sahil = json.loads(sahil)
    elaus = json.loads(elaus)
    comments = sahil + elaus
    
feature_sets = list(lexical_stuff(comments))

classifications = [predict_authors(fvs).labels_ for fvs in feature_sets]
results = classifications[0]
res_list = []
for _ in range(10):
    if results[0] == 0:
        results = 1 - results
    res_list.append((sum(results[:len(sahil)])/float(len(sahil))))
print "Accuracy = " + str(np.median(res_list))
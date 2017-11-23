# class BagOfWordsModel(object):
#     def __init__(self, filename):
from collections import Counter
import json

def main():
    with open('./data/vrckid.data', 'r') as f:
        sahil = f.read()
        sahil = json.loads(sahil)
        bag = Counter()
        for comment in sahil:
            for word in comment.split():
                bag[word] += 1
        print len(bag)
        #training = sahil[:int(len(sahil) * 0.7)]
        #test = sahil[:]



if __name__ == '__main__':
    main()
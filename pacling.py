from __future__ import division
import string
import nltk
from collections import Counter
import os

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


pacling = Pacling()
# print pacling.classify("tacosa", "salad")
# print pacling.classify("salad", "salad")
# print pacling.classify("yeah buddy", "yeah poop")
# print pacling.classify("vrckid is the best", "vrckid is the worst")
# print pacling.classify("sophia", "denice")
# print pacling.classify(" whoa whoa whoa whoa whoa ", " whoa ")


#print pacling.classify("Hurricane pike is instant at least so the storm can't zip away like he can with the autos projectile. Commenting on this late but I'm a senior CS major and took 208 on campus and I can honestly say it's one of my top 3 class. Learned an absolute shitton and made me better at problem solving.", "This post was removed due to breaking our giveaway rules\n\n>Giveaways are sometimes allowed if they're simply accompanying a post that has a different purpose to it, with the giveaway on the side (and not in the submission title).")

list_users = os.listdir('./data')
list_users = [a[:-5] for a in list_users]
print list_users
# with open('./data/vrckid.data', 'r') as f:
#     data = f.read()
#     import json
#     data = json.loads(data)
#     print pacling.classify('\n'.jo(data[:len(data)/2]), '\n'.join(data[len(data)/2:]))
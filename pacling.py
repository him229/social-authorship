from __future__ import division
import string


class Pacling:
    def __init__(self):
        pass

    def build_frequency_profile(self, s, n=2):
        # build bigram frequency map
        #[(a,b) for a in string.ascii_lowercase for b in string.ascii_lowercase]
        chars = string.ascii_lowercase + " "
        bigrams = {(a, b): 0 for a in chars for b in chars}
        for i in range(0, len(s) - n):
            bigrams[(s[i], s[i + 1])] += 1 
        # if we wanna limit profile size we can pick random bigrams to remove
        return bigrams

    def classify(self, author_string, test_string):
        n = 2
        pa = self.build_frequency_profile(author_string, 2)
        pt = self.build_frequency_profile(test_string, 2)
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
        # this returns a disimilarity score, we need to make it a percentage.
        # create the worst case similarity and divide the total by it?
        # number of bigrams / (total f1 + f2 / 2)
        return abs(1 - (total / worst_possible))


pacling = Pacling()
print pacling.classify("tacosa", "salad")
print pacling.classify("salad", "salad")
print pacling.classify("yeah buddy", "yeah poop")
print pacling.classify("vrckid is the best", "vrckid is the worst")
print pacling.classify("sophia", "denice")
print pacling.classify(" whoa whoa whoa whoa whoa ", " whoa ")

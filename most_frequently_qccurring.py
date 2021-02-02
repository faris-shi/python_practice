"""
Determining the Most Frequently Occurring Items in a Sequence
"""
from collections import Counter

words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]


words_counter = Counter(words)

print('The most 3 frequently occurring items:' , words_counter.most_common(3))

print(words_counter)
print('all occurs:', {key:value for key, value in words_counter.items()})


morewords = ['why','are','you','not','looking','in','my','eyes']
# to increase the words count of morewords to words_counter.
words_counter.update(morewords)
print(words_counter)
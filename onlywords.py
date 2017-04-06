# Author: Blake Conrad
# Only Get 'W'ords from a nasty string

import collections, re
texts = ['John likes to watch movies. Mary likes too.','John also likes to watch football games.']
bagsofwords = [ collections.Counter(re.findall(r'\w+', txt)) for txt in texts]
sumbags = sum(bagsofwords, collections.Counter())

print bagofwords[0]
print bagofwords[1]
print sumbags

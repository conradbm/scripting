# Author: Blake Conrad
# A simple way to get a sorted list of words and their correspding counts quickly.
# This can be changed quickly to Descending as well.

counts = Counter([i for i in ["The", "The", "cat", "jumpted", "over", "a","lazy","lazy","dog","dog,"a","a","a","a","a"]])
counts = sorted(counts.items(), key=lambda x:x[1]) 
counts.sort(key=lambda x:x[1], reverse=True)
counts

#listWords.py

hamlet = open('hamlet.txt','r').read()
hamlet = hamlet.lower()
for i in '!"#$%&*()+-,./:<>=?@[\\]^_‘{|}~\';':
    hamlet = hamlet.replace(i,' ')
words = hamlet.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())

#排序
items.sort(key=lambda x: x[1],reverse=True)

for i in range(len(items)):
    word,count = items[i]
    print("{0:<20}{1:>10}".format(word,count))
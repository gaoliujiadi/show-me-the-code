#statisticsFilesWords.py

import glob

files = glob.glob(r'needToStatistcs\*.txt')

def fromFilesToText(files):
    text = ''
    for i in range(len(files)):
        aFile = files[i]
        with open(aFile,'r',encoding='ansi') as f:
            text = text + f.read()
    return text

def sortWords(text):
    for i in '!"#$%&*()+-,./:<>=?@[\\]^_‘{|}~\';':
        text = text.replace(i,' ')
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1],reverse=True)
    return items

def main():
    text = fromFilesToText(files)
    items = sortWords(text)
    print('{0:<10}{1:>10}'.format('word','count'))
    for item in items[:10]:
        word,count = item
        print('{0:<10}{1:>10}'.format(word,count))

main()
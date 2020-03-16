#findTheFilteredWord.py
import jieba
text = input('Enter:')
words = []
for word in jieba.cut(text):
    words.append(word)
with open('filtered_words.txt','r',encoding='utf-8') as f:
    for i in range(len(words)):
        for line in f:
            #print(words[i])
            if line[:-1] == words[i]:
                words[i] = '*' * len(words[i])
        f.seek(0)
sum = ''.join(words)
print(sum)
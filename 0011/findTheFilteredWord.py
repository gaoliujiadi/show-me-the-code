#findTheFilteredWord.py
import jieba
text = input('Enter:')
flag = True
with open('filtered_words.txt','r',encoding='utf-8') as f:
    for word in f:
        for i in jieba.cut(text):
            #print(word[:-1])
            if i == word[:-1]:
                print('\nFreedom')
                flag = False
if flag:
    print('\nHuman Rights')
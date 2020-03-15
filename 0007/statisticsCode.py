#statisticsCode.py

with open('CalPiV2.py','r',encoding='utf-8') as f:
    i = 0
    comments = 0
    space = 0
    for line in f:
        i = i + 1
        if line[0] == '#':
            comments = comments + 1
        elif line == '\n':
            space = space + 1
        else:
            continue
    print('共{0}行，注释{1}行，空行{2}行。'.format(i,comments,space))
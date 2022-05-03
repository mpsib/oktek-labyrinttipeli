import random

#monia reittejä eri paikkoihin
stage = [['d ', 'rd', 'r ', 'rd', 'd ', 'rd', 'r ', 'd ', 'r ', 'r ', 'd ', 'd ', 'rd', 'r ', 'd '],
         ['d ', 'r ', '  ', 'd ', 'r ', '  ', 'rd', 'rd', 'r ', 'r ', '  ', 'd ', '  ', 'd ', 'd '],
         ['r ', 'rd', 'r ', 'r ', 'rd', 'r ', 'd ', 'r ', 'd ', 'rd', 'r ', 'rd', 'r ', 'rd', '  '],
         ['d ', 'd ', 'r ', 'd ', 'r ', '  ', 'd ', 'd ', 'd ', 'd ', 'r ', '  ', 'd ', 'rd', '  '],
         ['d ', 'rd', '  ', 'rd', 'r ', 'rd', '  ', 'd ', 'd ', 'r ', 'r ', 'r ', 'd ', 'd ', 'd '],
         ['d ', 'd ', 'rd', '  ', 'd ', 'rd', 'd ', 'd ', 'r ', 'rd', 'r ', 'd ', 'dr', '  ', 'd '],
         ['r ', 'r ', 'rd', 'rd', '  ', '  ', 'd ', 'rd', '  ', 'd ', 'rd', '  ', 'r ', 'd ', 'd '],
         ['rd', '  ', 'd ', 'rd', 'r ', '  ', 'd ', 'd ', 'rd', '  ', '  ', 'rd', 'rd', 'r ', 'd '],
         ['d ', 'r ', '  ', 'rd', 'd ', 'rd', '  ', 'dr', 'd ', 'r ', 'r ', '  ', 'r ', '  ', 'd '],
         ['r ', 'r ', 'r ', '  ', 'r ', 'r ', 'r ', '  ', 'r ', 'r ', 'r ', 'r ', 'r ', 'r ', '  ']]

#simply connected eli kaikki seinät ovat yhteydessä kentän reunaan
#ja mistä tahansa ruudusta on vain yksi reitti maaliin
stageSC=[['d ', 'rd', 'r ', 'rd', 'd ', 'rd', 'r ', '  ', 'r ', 'r ', 'd ', 'd ', 'rd', 'r ', 'd '],
         ['d ', 'r ', '  ', 'd ', 'r ', '  ', 'rd', 'rd', 'r ', 'r ', '  ', 'd ', '  ', 'd ', 'd '],
         ['r ', 'rd', 'r ', 'r ', 'rd', 'r ', 'd ', 'r ', 'd ', 'rd', 'r ', 'rd', 'r ', 'rd', '  '],
         ['d ', 'd ', 'r ', 'd ', 'r ', '  ', 'd ', 'd ', 'd ', 'd ', 'r ', '  ', 'd ', 'rd', '  '],
         ['d ', 'rd', '  ', 'rd', 'r ', 'rd', '  ', 'd ', 'd ', 'r ', 'r ', 'r ', '  ', 'd ', 'd '],
         ['d ', '  ', 'rd', '  ', 'd ', 'rd', 'd ', 'd ', 'r ', 'rd', 'r ', 'd ', 'dr', '  ', 'd '],
         ['r ', 'r ', 'rd', 'rd', '  ', '  ', 'd ', 'rd', '  ', 'd ', 'rd', '  ', 'r ', 'd ', 'd '],
         ['rd', '  ', 'd ', 'rd', 'r ', '  ', 'd ', 'd ', 'rd', '  ', '  ', 'rd', 'rd', 'r ', 'd '],
         ['d ', 'r ', '  ', 'rd', 'd ', 'rd', '  ', 'd ', 'd ', 'r ', 'r ', '  ', 'r ', '  ', 'd '],
         ['r ', 'r ', 'r ', '  ', '  ', 'r ', 'r ', '  ', 'r ', 'r ', 'r ', 'r ', 'r ', 'r ', '  ']]

#randomized stage that can be unsolvable
def randomizedStage():
    stage = [ [], [], [], [], [], [], [], [], [], [] ]
    for j in range(10):
        for i in range(15):
            string = ''
            randR = random.randint(1, 100)
            randD = random.randint(1, 100)
            if i < 14:
                if randR >= 40:
                    string += 'r'
            if j < 9:
                if randD >= 40:
                    string += 'd'
            stage[j].append(string)
    return stage

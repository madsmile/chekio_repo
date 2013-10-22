__author__ = 'Litvinov'
#python3.3 is inside
def checkio(els):
    temp = 0
    for x in range(3):
        temp += els[x]
    els = temp
    return els

if checkio([1, 2, 3, 4, 5, 6]) == 6:
    print('Done!')
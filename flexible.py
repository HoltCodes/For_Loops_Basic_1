#Flexible Counter- Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 16
mult = 4

for x in range(lowNum,highNum + 1):
  if x % mult == 0:
    print(x)
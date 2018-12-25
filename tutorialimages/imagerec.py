from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from statistics import mean
from collections import Counter

def createExamples():
    numberArrayExamples = open('numArrEx.txt', 'a')
    numbersWeHave = range(0, 10)
    versionsWeHave = range(1, 10)
    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVer) + '.png'
            ei = Image.open(imgFilePath)
            eiar = str(np.array(ei).tolist())
            numberArrayExamples.write(str(eachNum) + '::' + eiar + '\n')

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

def whatNumIsThis2(filePath):
    matchedArr = []
    loadExamples = open('numArrEx.txt', 'r').read()
    loadExamples = loadExamples.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iar1 = iar.tolist()
    inQuestion = str(iar1)
    
    for eachExample in loadExamples:
        try:
            splitExample = eachExample.split('::')
            currentNum = splitExample[0]
            currentArr = splitExample[1]
            eachPixExample = currentArr.split('],')
            eachPixInQ = inQuestion.split('],')
            
            x = 0
            while x<len(eachPixExample):
                if eachPixExample[x] == eachPixInQ[x]:
                    matchedArr.append(int(currentNum))
                x+=1
        except Exception as e:
            print(str(e))
    x = Counter(matchedArr)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]



    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()
    print(x)


whatNumIsThis('test.png')

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from collections import Counter

def createExamples():
    numbers = open('numberArr', 'a')
    for i in range(0, 10):
        for j in range(1, 10):
            img = Image.open('images/numbers/' + str(i) + '.' + str(j) + '.png')
            iar = str(np.array(img).tolist())
            numbers.write(str(i) + '::' + iar + '\n')

def threshold(imageArray):
    balanceArr = []
    newArr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            balanceArr.append(mean(eachPix[:3]))
    balance = mean(balanceArr)
    for eachRow in newArr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) < balance:                
                eachPix[0], eachPix[1], eachPix[2], eachPix[3] = 255, 255, 255, 255
            else:
                eachPix[0], eachPix[1], eachPix[2], eachPix[3] = 0, 0, 0, 255
            
def identifyNum(filePath):
    counts = []
    img = Image.open(filePath)
    i_np = np.array(img)
    iar = str(i_np.tolist())
    iar2 = iar.split('],')
    
    loadExamples = open('numberArr', 'r').read().split('\n')
    for example in loadExamples:
        if len(example) > 1:
            num = example[0]
            pixels = example[3:].split('],')
            for i in range(len(iar2)):
                if iar2[i] == pixels[i]:
                    counts.append(int(num))
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
    print(Counter(counts))
    counts = sorted(Counter(counts).items())
    x, y = zip(*counts)
    ax2.bar(x, y)
    ax1.imshow(i_np)
    plt.show()
    
img = Image.open('test.png')
iar = np.array(img)
threshold(iar)
identifyNum('test.png')
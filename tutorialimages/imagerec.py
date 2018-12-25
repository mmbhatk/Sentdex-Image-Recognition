from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from statistics import mean

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
    return newArr

i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

threshold(iar2)
threshold(iar3)
threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan = 4, colspan = 3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan = 4, colspan = 3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan = 4, colspan = 3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan = 4, colspan = 3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)
plt.show()
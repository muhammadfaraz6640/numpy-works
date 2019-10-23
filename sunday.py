# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:47:25 2019

@author: Haroon Traders
"""

import numpy as np
text="my name is faraz ansar and i am the student of software engineering"
i=text.split()
arr=np.array(i)
pr=print
pr(arr)
lnt=np.vectorize(len) # apply on strings----> for a in arr:  if len(a)<5 print(a)
print(arr[lnt(arr)<5])
print(arr[[2,3,4]])  #fancy slicing
# 4d array zero data
abc=np.zeros((5,4,3,2))
abc[2,0]=5
abc[:,:,0,:]=2
abc[:,:,:,1]=9
print(abc)
print(abc.ndim)
print(abc.shape)
print(abc[4,1,2])
ab=np.zeros((2,3,2,3))
print(ab)
ab[1,1,0,1:3]=7
print(ab)
ad=np.array([1,-2,3,4,5])
c=np.fabs(ad)
print(c)
print(np.fabs(ad))  #fabs and abs function return positive
print(np.sqrt(c))
print(np.square(ad))
b=np.arange(1,11)
print(np.where(b>5,b+1,b*10))
#np.where is just like conditional operators in c and c++
print(np.mean(c))
print(np.cumsum(c))
print(np.std(c))
print(np.cumprod(c))
e=b<3
print(e)
print(np.sum(e))  #counting the trues
print(np.any(e))
v=b==15
print(np.all(e))  #means all the values are true or not? returns boolean
f=np.arange(11,1,-1)
print(f)
print(np.sort(f))
# dta analysis and handling using pandas
aa=list(["faraz","laiba","faraz","abacus"])
print(np.unique(aa))  # as well as sorts the data
name="faraz"
'''
np.save("C:/Users/Haroon Traders/Desktop/New folder",e)
np.load('newfolder.npy')
np.save('faraz',e)

aab=np.arange(10,0,-1)
cc=np.split(aab,[2,6])
print(cc[0])
print(np.split(aab,[2,6]))
aab.reshape(2,5)
print(aab)
np.random.seed(0)
print(np.random.rand(3))
np.random.seed(0)
print(np.random.rand(3))
from matplotlib import pyplot as plt
im=plt.imread("C:/Users/Haroon Traders/Pictures/untitled.png")
print(np.shape(im))
#n=np.array(im)
#print(n)
#plt.imshow(im)
# load 20 images 
# pil library
photos=np.zeros((20,312,500,4))
#photos[0]=im
print(np.shape(photos))
#print(photos)
'''
from PIL import Image as im
from matplotlib import pyplot as plt
import numpy as np
import os
def filecount(root):
    fcount=len([x for x in os.scandir(root)])
    print(fcount)
    pat=list(str([]))
    for dirname,subdirlist,filelist in os.walk(root):
        print("name of directory : "+dirname)
        for fname in filelist:
            #print(fname)
            p=os.path.abspath(fname)
            pat.append(p)
    pat.pop(0)
    pat.pop(0)
    return pat
def resize(arr_pics):
    for i in range(20):
        #d=im.open(arr_pics[i])
try:
    def main():
        dire="photos"
        p=filecount(dire)
except:
        print("error")
    
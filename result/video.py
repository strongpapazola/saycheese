import cv2
import numpy as np
from subprocess import Popen, PIPE
import time
import sys
import time

def shell(cmd):
 return Popen(cmd, shell=True, stdout=PIPE).stdout.read().decode('utf-8')

img_array = []
for filename in shell("find * -type f | grep png").splitlines():
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    shell('rm '+filename)


out = cv2.VideoWriter('video/'+str(time.time()).split('.')[0]+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

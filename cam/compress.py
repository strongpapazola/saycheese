from PIL import Image
from subprocess import Popen, PIPE
import time
import sys

def shell(cmd):
 return Popen(cmd, shell=True, stdout=PIPE).stdout.read().decode('utf-8')

a = shell("find * -type f | grep png").splitlines()
lena = len(a)
for i in range(0, lena):
# sys.stdout.write(str(lena))
# sys.stdout.flush()
# print(str(lena)+" : "+str(a[i]), end='\r')
 print(str(lena)+" : "+str(a[i]))
 try:
  im = Image.open(str(a[i]))
  im.save(str(a[i]), format="PNG", quality=50)
  shell('mv '+str(a[i])+' ../result/')
 except:
  pass
 lena = lena - 1

# print(i)

## CST 205 -- Lab #9
#Nicholas Saunders
import os #to allow access to os.path.abspath(__file__) and os.path.dirname

def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')

#Problem 1
def clip(source, start, end):
  lenNewClip = end - start
  lenSource = getLength(source)
  newClip = makeEmptySound(lenNewClip,44100)
  index = 0
  for i in range(start,end):
    value = getSampleValueAt(source,i)
    setSampleValueAt(newClip,index,value)
    index += 1
  return(newClip)

#Problem 2
def copy(source, target, start):
  lensource = getLength(source)
  for i in range(0, lensource):
    value = getSampleValueAt(source,i)
    setSampleValueAt(target,start,value)
    start += 1
  return target 

#Problem 3
def soundCollage():
  s1 = makeSound(getMediaPath() + 'lumberjacksong.wav')
  s2 = makeSound(getMediaPath() + 'Spanish Inquision.wav')
  s3 = makeSound(getMediaPath() + 'Parrot.wav')
  s4 = makeSound(getMediaPath() + 'Witch.wav')
  s5 = makeSound(getMediaPath() + 'Python Insults.wav')
  
  newClip1 = clip(s1,1222020,1695516)#lumberjack clip
  newClip2 = clip(s2,88572,412848) #spanish clip
  newClip3 = clip(s3,830020,1650000) # dead parrot clip
  newClip4 = clip(s4,125,2836054) #Witches are made of wood clip
  newClip5 = clip(s5,261738,651987) #Python Insult clip
  
  len1 = getLength(newClip1) 
  len2 = getLength(newClip2)
  len3 = getLength(newClip3)
  len4 = getLength(newClip4)
  len5 = getLength(newClip5)
  
  lenOfFullClip = len1+len2+len3+len4+len5+100000
  
  emptyClip= makeEmptySound(lenOfFullClip,44100) 
  ## empty clip w/ length of smaller clips together
  
  edit1 = copy(newClip1,emptyClip,0) #lumberjack clip
  edit2 = copy(newClip2,edit1,480000) #spanish clip
  edit3 = copy(newClip3,edit2,803904) #dead parrot clip
  edit4 = copy(newClip4,edit3,1653312) #witchs are made of wood
  edit5 = copy(newClip5,edit4,4520064) #Python Isult clip
  collage = edit5
  explore(collage)
  
  
#Problem 4
def reverse(sound):
  return true
  
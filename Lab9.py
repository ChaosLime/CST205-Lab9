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
  lenSource = getLength(source)
  for i in range(0, lenSource):
    value = getSampleValueAt(source,i)
    setSampleValueAt(target,start,value)
    start += 1
  return target 

#Problem 3
def soundCollage():
  #asks user to set to current directory path to current directory
  setMediaPathToCurrentDir() 
  s1 = makeSound(setMediaPath() + 'lumberjacksong.wav')
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
  lenOfSilence = int(0.5*getSamplingRate(newClip1))
  #each clips sample rating is 44100, therefore newClip1 can represent all 5 clips.
  #this can only work if all clips have the same sample rate.
  #also only works with 5 clips total.
  lenOfFullClip = len1+len2+len3+len4+len5+lenOfSilence*5
  
  emptyClip= makeEmptySound(lenOfFullClip,44100) 
  ## empty clip w/ length of smaller clips together
  
  edit1 = copy(newClip1,emptyClip,0) #lumberjack clip
  edit2 = copy(newClip2,edit1,480000) #spanish clip
  edit3 = copy(newClip3,edit2,803904) #dead parrot clip
  edit4 = copy(newClip4,edit3,1653312) #witchs are made of wood
  edit5 = copy(newClip5,edit4,4520064) #Python Isult clip
  collage = edit5
  explore(collage)
  writeSoundTo(collage, getMediaPath() + 'soundCollage.wav')
  
##Problem 4  
def sound():
  #Call sound to run reverse()
  #s = makeSound(getMediaPath() + 'loser.wav')
  s = (makeSound(pickAFile()))
  explore(reverse(s))

#Problem 4
def reverse(sound):
  lenSource = getLength(sound)
  index = lenSource-1
  reversedSound = makeEmptySound(lenSource,44100)

  for i in range(0,lenSource):
    tempValue = getSampleValueAt(sound,i)
    setSampleValueAt(reversedSound,index,tempValue)
    index -= 1
  return reversedSound  



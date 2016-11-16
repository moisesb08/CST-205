def makeCollage():
  """ Makes an empty picture and copies pictures in specific locations, saves image
      Effects are added to the pictures
  
  Returns the target picture, target
  """
  target = makeEmptyPicture(2550, 3300)
  picP = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\P.jpg")
  picY = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\Y.jpg")
  picT = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\T.jpg")
  picH = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\H.jpg")
  picO = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\O.jpg")
  picN = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\N.jpg")
  me = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\me.jpg")
  cat = makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\cat.jpg")
  smallO = shrink(makePicture("C:\Users\\Moises\\Desktop\\Week 2\\Lab 5\\OO.jpg"))
  smallO = mirrorXY(rotatePic(smallO))
  for i in range(10):
    for j in range(7):
      target = pyCopy(smallO, target, i*298, j*531)
  target = pyCopy(shrink(picP), target, 139, 1000)
  target = pyCopy(Artify(shrink(picY)), target, 942, 1000)
  target = pyCopy(sepiaTone(shrink(picT)), target, 1745, 1000)
  target = pyCopy(sepiaTone(shrink(picH)), target, 139, 1636)
  target = pyCopy((shrink(picO)), target, 942, 1636)
  target = pyCopy(Artify(shrink(picN)), target, 1745, 1636)
  target = pyCopy(me, target, 942, 2000)
  target = pyCopy(cat, target, 1745, 2000)
  return target

def pyCopy(source, target, targetX, targetY):
  """ Makes a copy of a picture onto a target picture at a specified location
  
  Returns the target picture, target
  source: a picture that will be copied
  target: a picture source will be copied to
  targetX: int value of placement x location
  targetY: int value of placement y location
  """
  targetW = getWidth(target)
  targetH = getHeight(target)
  sourceW = getWidth(source)
  sourceH = getHeight(source)
  if(targetX > targetW or targetY > targetH):
    return target
  xMax = min(targetX + sourceW, targetW)
  yMax = min(targetY + sourceH, targetH)
  x = 0
  for destX in range(targetX, xMax):
    y = 0
    for destY in range(targetY, yMax):
      p = getPixel(source, x, y)
      destPixel = getPixel(target, destX, destY)
      setColor(destPixel, getColor(p))
      y += 1
    x += 1
  return target

def reflectX(pic):
  """ Flips half the picture about the x-axis
  
  Returns the edited picture, pic
  pic: a picture that will be manipulated
  """
  width = getWidth(pic)
  for x in range(width/2, width):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, width - x - 1, y)
      destinationPixel = getPixel(pic, x,y)
      setColor(destinationPixel, getColor(pixel))
  return pic
  
def reflectY(pic, reverse = false):
  """ Flips half the picture about the y-axis
      Default is TopBottom
      
  Returns the edited picture, pic
  pic: a picture that will be manipulated
  reverse: boolean which indicated if the flip is BottomTop
  """
  height = getHeight(pic)
  if(reverse):
    start = 0
    end = height/2
  else:
    start = height/2
    end = height
  for x in range(0, getWidth(pic)):
    for y in range(start, end):
      pixel = getPixel(pic, x, height - y - 1)
      destinationPixel = getPixel(pic, x,y)
      setColor(destinationPixel, getColor(pixel))
  return pic

def mirrorXY(pic):
  """ Flips half the picture about the y-axis Top to Bottom
      Flips half the picture about the x-axis
      Calls the reflectX and reflectY functions
  Returns the edited picture, pic
  pic: a picture that will be manipulated
  """
  pic = reflectY(reflectX(pic))
  return pic

def rotatePic(pic):
  """ Rotates an image 90 degrees counterclockwise
  
  Returns the destination picture, destPic
  pic: a picture that will be rotated
  """
  destHeight = getWidth(pic)
  destWidth = getHeight(pic)
  destPic = makeEmptyPicture(destWidth, destHeight)
  for x in range (0, destWidth):
    for y in range(0, destHeight):
      p = getPixel(pic, destHeight - y - 1, x)
      destPixel = getPixel(destPic, x, y)
      setColor(destPixel, getColor(p))
  return destPic

def shrink(pic, factor = 2):
  """ Shrinks picture by half
      Default factor is 2 but can be any integer greater than 0
  
  Returns the destination picture, destPic
  pic: a picture that will be shrunk
  factor: an integer greater than 0 used as the shrink factor
  """
  width = getWidth(pic)
  height = getHeight(pic)
  destPic = makeEmptyPicture(width/factor, height/factor)
  destWidth = getWidth(destPic)
  destHeight = getHeight(destPic)  
  for x in range(0, width, factor):
    for y in range(0, height, factor):
      p = getPixel(pic, x, y)
      if(destWidth > x/factor and destHeight > y/factor):
        destP = getPixel(destPic, x/factor, y/factor)
        setColor(destP, getColor(p))
  return destPic

def betterBnW(pic):
  """ Converts each pixel of a selected picture to grayscale
      using a luminance formula
  
  Returns the black and white picture
  pic: the picture to be manipulated
  """
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    grayValue = (r*0.299 + g*0.587 + b*0.114)
    setRed(p, grayValue)
    setGreen(p, grayValue)
    setBlue(p, grayValue)
  return pic

def sepiaTone(pic):
  """ Creates a sepia tone image of the specified image using the betterBnW functions
  
  Returns the sepia tone picture
  pic: the picture to be manipulated
  """
  betterBnW(pic)
  for p in getPixels(pic):
    r = getRed(p)
    b = getBlue(p)
    if r < 63:
      setRed(p, r * 1.1)
      setBlue(p, b * .9)
    elif r < 192:
      setRed(p, r * 1.15)
      setBlue(p, b * .85)
    else:
      if(r*1.08 > 255):
        setRed(p, 255)
      else:
        setRed(p, r * 1.08)
      setBlue(p, b * .93)
  return pic

def artify(pic):
  """ Creates an artsy effect on a picture. It does this by selecting certain range
      of values for each color (i.e., red, green, blue) which is replaced by a certain
      value
  
  Returns the artifyed picture
  pic: the picture to be manipulated
  """
  for p in getPixels(pic):
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    
    # Modify Red
    if r < 64:
      setRed(p, 10)
    elif r < 128:
      setRed(p, 120)
    elif r < 192:
      setRed(p, 180)
    else:
      setRed(p, 255)
    
    # Modify Green
    if g < 64:
      setGreen(p, 10)
    elif g < 128:
      setGreen(p, 120)
    elif g < 192:
      setGreen(p, 180)
    else:
      setGreen(p, 255)
    
    # Modify Blue
    if b < 64:
      setBlue(p, 10)
    elif b < 128:
      setBlue(p, 120)
    elif b < 192:
      setBlue(p, 180)
    else:
      setBlue(p, 255)
  return pic
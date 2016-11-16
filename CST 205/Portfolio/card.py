def card():
  """ Creates a collage of three images with a gradient fading orange to black and text.
      The text displays a message for Thanksgiving.
  
  Returns the final Thanksgiving card picture.
  """
  leavesPic = makePicture("C:\\Users\\Moises\\Desktop\\Week 3\\Lab 7\\pics\\fall.jpg")
  turkeyPic = shrink(makePicture("C:\\Users\\Moises\\Desktop\\Week 3\\Lab 7\\pics\\turkeyA.jpg"))
  pumpkinPic = shrink(makePicture("C:\\Users\\Moises\\Desktop\\Week 3\\Lab 7\\pics\\pumpkins.jpg"), 5)
  pic = makeEmptyPicture(1920,1080, makeColor(230,150,0))
  
  # Fade to black
  pic = fadeBlack(pic)
  
  # Add white bottom corners
  addOvalFilled(pic, 1670, 830, 600, 600, white)
  pic = reflectX(pic, true)
  
  # Add turkey, pumpkins, and leaves
  pic = pyCopy(turkeyPic, pic, 1780, 930)
  whiteCanvas = makeEmptyPicture(1920,1080)
  whiteCanvas = pyCopy(pumpkinPic, whiteCanvas, 10, 930)
  pic = chromakey(whiteCanvas, pic, color=white)
  pic = chromakey(leavesPic, pic, 0 , 0, 180, white)
  
  # Add text
  title = makeStyle(sansSerif, bold, 150)
  subtitle = makeStyle(serif, italic, 80)
  thanks = "Happy Thanksgiving!"
  enjoy = "Be thankful and enjoy this day."
  addTextWithStyle(pic, 190, 550, thanks, title, white)
  addTextWithStyle(pic, 460, 750, enjoy, subtitle, white)
  return pic
  
def fadeBlack(pic, fadeSize = 4):
  """ Fades the top row colors to black with a specified size.
  
  Returns the faded picture
  pic: picture to be manipulated
  fadeSize: the size of the fade, the larger the value the slower the fade
  """
  w = getWidth(pic)
  h = getHeight(pic)
  newColor = black
  for x in range(0, w):
    index = 0;
    for y in range(0, h-1):
      p = getPixel(pic, x, y)
      pNext = getPixel(pic, x, y+1)
      if index%fadeSize == 0:
        newColor = makeColor(max(0, getRed(p)-1), max(0, getGreen(p)-1), max(0, getBlue(p)-1))
      setColor(p, newColor)
      setColor(pNext, newColor)
      index += 1
  return pic          
  
def chromakey(fore, back, targetX=0, targetY=0, tolerance = 100, color=green):
  """ uses two images to create a new image which represents the background image and the foreground
      without the specified color (default color is green).
  
  Returns the background with the non-green parts of the foreground
  fore: the foreground picture which is color checked
  back: the background picture, no color check
  targetX: where on the width the checking begins
  targetY: where on the height the checking begins
  tolerance: this is how much of the color difference is accepted
  color: this is the color that will be replaced
  """
  xMax = getWidth(back)
  yMax = getHeight(back)
  w = getWidth(fore)
  h = getHeight(fore)
  for y in range(min(targetY, h), h):
    if y >= yMax:
      break
    for x in range(min(targetX, w), w):
      if x >= xMax:
        break
      backPixel = getPixel(back, x, y)
      backColor = getColor(backPixel)
      forePixel = getPixel(fore, x, y)
      foreColor = getColor(forePixel)
      if distance(foreColor, color) > tolerance:
        #Catch case if the background image is smaller than the foreground image.
        if x >= xMax or y >= yMax:
          setColor(forePixel, black)
        else:
          forePixel = getPixel(fore, x, y)
          foreColor = getColor(forePixel)
          setColor(backPixel, foreColor)     
  return back
  
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

def reflectX(pic, reverse = false):
  """ Flips half the picture about the x-axis
  
  Returns the edited picture, pic
  pic: a picture that will be manipulated
  """
  width = getWidth(pic)
  if(reverse):
    start = 0
    end = width/2
  else:
    start = width/2
    end = width
  for x in range(start, end):
    for y in range(0, getHeight(pic)):
      pixel = getPixel(pic, width - x - 1, y)
      destinationPixel = getPixel(pic, x,y)
      setColor(destinationPixel, getColor(pixel))
  return pic
  
def shrink(pic, factor = 2):
  """ Shrinks picture by half, saves image
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
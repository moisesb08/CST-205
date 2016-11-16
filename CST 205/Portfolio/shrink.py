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
  
def lineDrawing(pic, tolerance = 20):
  """Creates a black and white line drawing of any picture
     If the difference in luminance between the current pixel and right pixel
     as well as the difference in luminance between the current pixel and below pixel
     are within the tolerance then the pixel color is set to white, otherwise black
     
  pic: this is the picture that will be manipulated
  tolerance: this is the amount of difference in luminance that is accepted
  """
  w = getWidth(pic)
  h = getHeight(pic)
  destPic = makeEmptyPicture(w,h)
  for x in range(0, w-1):
    for y in range(0, h-1):
      rightP = getPixel(pic, x+1, y)
      belowP = getPixel(pic, x, y+1)
      currentP = getPixel(pic, x, y)
      if abs(lum(currentP)-lum(rightP)) < tolerance and abs(lum(currentP)-lum(belowP)) < tolerance:
        setColor(getPixel(destPic, x, y), white)
      else:
        setColor(getPixel(destPic, x, y), black)
  return destPic

def lum(pixel):
  """Returns the luminance of the pixel
  
  pixel: the pixel to be checked
  """
  return getRed(pixel)*0.299 + getGreen(pixel)*0.587 + getBlue(pixel)*0.114
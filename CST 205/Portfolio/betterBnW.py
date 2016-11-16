def betterBnW(pic):
  """ Converts each pixel of a selected picture to grayscale
      using a luminance formula
  
  Returns the black and white picture
  pic: picture to be manipulated
  """
  for p in getPixels(pic):
    grayValue = (getRed(p)*0.299 + getGreen(p)*0.587 + getBlue(p)*0.114)
    setRed(p, grayValue)
    setGreen(p, grayValue)
    setBlue(p, grayValue)
  return pic
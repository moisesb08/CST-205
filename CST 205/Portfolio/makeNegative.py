def makeNegative(pic):
  """ Creates the negative of the selected picture
  
  Returns the negative picture
  pic: the picture to be manipulated
  """
  for p in getPixels(pic):
    setRed(p,(255 - getRed(p)))
    setGreen(p,(255 - getGreen(p)))
    setBlue(p,(255 - getBlue(p)))
  return pic
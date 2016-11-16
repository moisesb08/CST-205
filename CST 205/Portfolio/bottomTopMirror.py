def bottomTopMirror(pic):
  """ Flips half the picture about the y-axis
      From bottom to top
      
  Returns the edited picture, pic
  pic: a picture that will be manipulated
  """
  height = getHeight(pic)
  for x in range(0, getWidth(pic)):
    for y in range(0, height/2):
      c = getColor(getPixel(pic, x, height - y - 1))
      destPixel = getPixel(pic, x,y)
      setColor(destPixel, c)
  return pic
def roseColoredGlasses(pic, strength = 0.5):
  """ Adds a rose pink tint to a selected picture
  
  Returns the rose colored picture
  pic: the picture to be manipulated
  strength: the amount of rose pink in the picture
  """
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p, r + (255 - r) * strength)
    setGreen(p, g + (102 - g) * strength)
    setBlue(p, b + (204 - b) * strength)
  return pic
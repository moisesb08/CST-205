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
def chromakey(fore, back, targetX=0, targetY=0, tolerance = 175, color = green):
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
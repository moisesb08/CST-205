def redEye(pic, xMin=0, xMax=0, yMin=0, yMax=0):
  """ Fixes the red eye color in picture
  
  Returns the picture with the red eye fixed
  pic: the picture to be manipulated
  xMin: Minimum x value to be checked
  xMax: Maximum x value to be checked
  yMin: Minimum y value to be checked
  yMax: Maximum y value to be checked
  """
  if(xMin > xMax or yMin > yMax):
    return
  if(xMin == 0 and xMax == 0 and yMin == 0 and yMax == 0):
    xMax = getWidth(pic)-1
    yMax = getHeight(pic)-1
  for x in range(xMin,xMax):
    for y in range(yMin,yMax):
      p=getPixel(pic,x,y)
      if distance(red,getColor(p)) < 190.0:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        grayValue = (r*0.299 + g*0.587 + b*0.114)
        setRed(p, (grayValue+50)/2)
        setGreen(p, (grayValue+30)/2)
        setBlue(p, (grayValue+35)/2)
  return pic
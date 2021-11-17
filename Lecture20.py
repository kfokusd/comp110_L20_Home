import image

def getRGB_diff(pix1, pix2):
    (r1, g1, b1) = pix1.getColorTuple()
    (r2, g2, b2) = pix2.getColorTuple()
    avg = ( abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2) ) / 3
    return avg
# End of getRGB_diff

img = image.Image("babyyoda.jpg")
nWidth = img.getWidth()
nHeight = img.getHeight()

# Create a window to hold the image
win = image.ImageWin(nWidth, nHeight)

img.draw(win)
win.exitonclick()
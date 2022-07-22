import cv2 as cv
import pandas as pd
import sys

img = cv.imread("colorpic.jpg")
index = ["officialColor","Color","Hex","r","g","b"]
color = pd.read_csv("colors.csv",names=index)
color.head()

def colorName(r,g,b):
    minimum = 20000
    for i in range(len(color)):
        sum = abs(r - int(color.loc[i,"r"])) + abs(g-int(color.loc[i,"g"])) + abs(b-int(color.loc[i,"b"]))
        if sum <= minimum:
            minimum = sum
            colName = color.loc[i,"Color"]
    return colName
# colorName(89, 39, 34)

r = g = b = xpos = ypos = 0
click = False
def draw(event,x,y,flags,param):
    global r,g,b,xpos,ypos,click
    if event == cv.EVENT_LBUTTONDBLCLK:
        click = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        
cv.namedWindow("Color_Picker")
cv.setMouseCallback("Color_Picker",draw)

while True:
    cv.imshow("Color_Picker", img)

    if click == True:
        print(colorName(r,g,b))
        text = colorName(r,g,b)
        cv.putText(img, text, (xpos,ypos) , 2, 1, (0,0,0), 2 , cv.LINE_AA)
        click = False
    if cv.waitKey(20) & 0xFF == 27:
        break




cv.destroyAllWindows()
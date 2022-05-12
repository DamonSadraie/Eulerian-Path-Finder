from calendar import c
from shutil import move
from graphics import *
import time
from maincode import SavedVar
from maincode import SavedAns

def initialize(coordinates,answer):
    print(answer)
    k=len(list(coordinates.keys())[0])
    #first we decide node size:
    nodeTxtSize=k-1
    #then we decide the display window size: first we get the max X and Y
    coordX_max=0
    coordY_max=0
    for i in coordinates.values():
        if i[0]>coordX_max:
            coordX_max=i[0]
        if i[1]>coordY_max:
            coordY_max=i[1]
    if coordX_max<coordY_max:
        for i in coordinates.keys():
                temp1=coordinates[i][0]
                coordinates[i][0]=coordinates[i][1]
                coordinates[i][1]=temp1
        temp2=coordX_max
        coordX_max=coordY_max
        coordY_max=temp2
    r=int(700/(4*coordX_max))
    gridY= (((4*coordY_max)-2)*r)+100
    gridX=(((4*coordX_max)-2)*r)+100
    font=int(2*r/k)
    display(gridX,gridY,font,r,coordinates)
    return


def display(gridX,gridY,font,r,coordinates):
    try:
        win = GraphWin("megaPint",gridX,gridY)
        win.setBackground("Black")
    # 4 letters size 10 = 20 r of node      so maybe k.size=2r   this works

    #txt= Text(coord,"node5")
    #txt.setTextColor('green')
    #txt.setSize(font)
    #txt.setFace('courier')
    #txt.draw(win)

        for i in coordinates.keys():
            nodeX=(((coordinates[i][0] * 4)-3) *r) + 50
            nodeY=(((coordinates[i][1] * 4)-3) *r) + 50
            j=i
            tempLength=len(j)
            for z in range(tempLength):
                j+="letter"+str(ord(j[0]))
                j=j[1:]
            exec(j + "_node = Circle(Point(nodeX,nodeY),r)")    #objects are made with var names from the keys
            exec(j + "_node.setOutline('White')")
            exec(j + "_node.draw(win)")
            exec(j + "_txt = Text(Point(nodeX,nodeY),i)")
            exec(j + "_txt.setTextColor('green')")
            exec(j + "_txt.setSize(font)")
            exec(j + "_txt.setFace('courier')")
            exec(j + "_txt.draw(win)")
        win.getMouse()
        win.close()
    except:
        print("No Error")


retrievedVar=SavedVar
retrievedAns=SavedAns
initialize(retrievedVar,retrievedAns)
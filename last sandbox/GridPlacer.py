from re import I
import VisCore
import maincode
import operator
from random import seed
from random import randint
from random import shuffle
seed(1)
def program(kmerList):
    n=len(kmerList[0])-1 
    mainGrid={}
    deb=maincode.DeBruijn(kmerList)
    ins=maincode.indegrees(deb)
    table=maincode.Table(deb)
    visCoreResult=VisCore.program(table,deb)
    relations=visCoreResult[1]
    deb=visCoreResult[0]
    listOfRails=visCoreResult[2]
    prioList=nodePrio(listOfRails,relations,n)
    for i in prioList:
        nextNode=i
        mainGrid=placer(deb,mainGrid,nextNode,ins)
    return mainGrid
def nodePrio(listOfRails,relations,n):
    prioList=[]
    for i in listOfRails:
        innerlist=i[list(i.keys())[0]]
        for j in innerlist[::-1]:
            prioList.insert(0,j)
    for i in relations.copy().keys():
        if not len(i)==n:
            del relations[i]
    relationsOrdered = dict( sorted(relations.items(),key=operator.itemgetter(1)))
    for i in relationsOrdered.keys():
        prioList.insert(0,i)
    return prioList
def placer(deb,mainGrid,nextNode,ins):
    if len(mainGrid.keys())==0:
        mainGrid[nextNode]=[1,1]
        return mainGrid
    if len(mainGrid.keys())==1:
        mainGrid[nextNode]=[2,1]
        return mainGrid
    surList=surf(mainGrid)
    minimum=100000000000000000000
    min2Center=100000000000000
    center=mainGridCenter(mainGrid)
    bestPlace=[]
    for i in surList:
        totalVectorLengthSquared=0
        x=i[0]
        y=i[1]
        centerVectorSquared=(float(x)-center[0])**2+(float(y)-center[1])**2 ###
        for j in mainGrid.keys():
            if j in deb.keys():
                if nextNode in deb[j]:   #'her d-devel'
                    x0=mainGrid[j][0]
                    y0=mainGrid[j][1]
                    totalVectorLengthSquared+=((x-x0)**2)+((y-y0)**2)
            elif j in ins.keys():
                if nextNode in ins[j]:   #'her d-devel'
                    x0=mainGrid[j][0]
                    y0=mainGrid[j][1]
                    totalVectorLengthSquared+=((x-x0)**2)+((y-y0)**2)
        if (totalVectorLengthSquared<minimum):
            minimum=totalVectorLengthSquared
            bestPlace=[x,y]
        elif totalVectorLengthSquared==minimum:   #new change here just delete 3 lines below and add or (totalVectorLengthSquared==minimum and randint(0,1)==1) 2above
            if (centerVectorSquared<min2Center) or (centerVectorSquared==min2Center and randint(0,1)==1):
                min2Center=centerVectorSquared
                bestPlace=[x,y]
    mainGrid[nextNode]=bestPlace
    if bestPlace[0]==0:
        for i in mainGrid.values():
            xr=i[0]
            yr=i[1]
            mainGrid[list(mainGrid.keys())[list(mainGrid.values()).index(i)]]=[xr+1,yr]
    if bestPlace[1]==0:
        for i in mainGrid.values():
            xr=i[0]
            yr=i[1]
            mainGrid[list(mainGrid.keys())[list(mainGrid.values()).index(i)]]=[xr,yr+1]
    return mainGrid
def surf(mainGrid):
    surList=[]
    gridDots=[]
    for i in mainGrid.values():
        gridDots.append(i)
    for i in gridDots:
        a=i[0]
        b=i[1]
        surList.append([a+1,b+1])
        surList.append([a+1,b])
        surList.append([a+1,b-1])
        surList.append([a,b+1])
        surList.append([a,b-1])
        surList.append([a-1,b+1])
        surList.append([a-1,b])
        surList.append([a-1,b-1])
    for i in gridDots:
        if i in surList:
            condition=True
            while condition==True:
                surList.remove(i)
                if i not in surList:
                    condition=False
    shuffle(surList)
    return surList
def mainGridCenter(mainGrid):
    coordX_max=0
    coordY_max=0
    for i in mainGrid.values():
        if i[0]>coordX_max:
            coordX_max=i[0]
        if i[1]>coordY_max:
            coordY_max=i[1]
    return [float((coordX_max+1)/2),float((coordY_max+1)/2)]
    


import maincode #isue#1 self

def railMain(table,N,deb):
    lineLengthMin=int(N/80)
    lineNodeCandidates=[]
    listOfRails=[]
    for i in table.keys():
        if table[i][0]==1 and table[i][1]==1 and deb[i]!=[i]:
            lineNodeCandidates.append(i)
    motor2=True
    while motor2==True:
        y=rails(lineNodeCandidates,deb,lineLengthMin)
        if not y=={}:
            listOfRails.append(y)
            for i in y[list(y.keys())[0]]:
                if i in lineNodeCandidates: #$$$#
                    lineNodeCandidates.remove(i)
        else:
            motor2=False
    return listOfRails
def rails(lineNodeCandidates,deb,lineLengthMin):
    listOfPossibleRails=[]
    for i in lineNodeCandidates:
        temp=train(i,lineNodeCandidates,deb,lineLengthMin)
        if temp != {}:
            listOfPossibleRails.append(temp)    #now, listOfRails has dictionaries in it. [ATT-AAA]=[path]
    maxx=0
    if listOfPossibleRails != []:
        maxx=0
        maxxPath={"temp":[]}
        for i in listOfPossibleRails:
            x=len(i[list(i.keys())[0]])
            if x>maxx:
                del maxxPath[list(maxxPath.keys())[0]]
                maxxPath=i
                maxx=x
    if not maxx == 0:
        return maxxPath
    else:
        return {}
def train(node,candidates,deb,n):
    length=0
    nodeX=node
    rail=[node]
    result={}
    motor1=True
    while motor1==True:
        if nodeX in candidates:
            candidates.remove(nodeX)
            nodeX=deb[nodeX][0]
            rail.append(nodeX)
            length+=1
        else:
            motor1=False
    if length>=n:
        railName=rail[0]+"-"+rail[-1]
        result[railName]=rail
        return result
    else:
        return {}
def railsInstall(deb,table):
    ins=maincode.indegrees(deb)
    N=len(list(table.keys()))
    listOfRails=railMain(table,N,deb)
    newIns=ins
    newDeb=deb
    newTable=table
    length=int(len(list((listOfRails[0]).keys())[0])/2)
    for i in listOfRails:
        a=(list(i.keys())[0])[:length]
        b=(list(i.keys())[0])[-length:]
        for j in i[(list(i.keys())[0])]:  #blindFix
            if j in newDeb.keys():
                del newDeb[j]
            if j in newIns.keys():
                del newIns[j]
            if j in newTable.keys():
                del newTable[j]
        if b in deb.keys():
            newDeb[(list(i.keys())[0])]=deb[b]
        if a in ins.keys():
            newIns[(list(i.keys())[0])]=ins[a]
        newTable[(list(i.keys())[0])]=[1,1]
    result= [newIns,newDeb,newTable,listOfRails]
    return result
def ntagram(deb,ins,relations):
    result=[[]] #list of (list of ntagram nodes)
    cutoff=23

    return
def deleteSelf(list):
    selfList=[]
    for i in list[0].copy().keys():
        if i in list[0][i]:
            list[0][i].remove(i)
            list[2][i][0]-=1
            selfList.append(i)
    for i in list[1].copy().keys():
        if i in list[1][i]:
            list[1][i].remove(i)
            list[2][i][1]-=1
            selfList.append(i)
    return[list[0],list[1],list[2],selfList]
def program(table,deb):
    railinstalled=railsInstall(deb,table)
    listOfRails=railinstalled[3]
    del railinstalled[3]
    selfDeleted=deleteSelf(railinstalled)
    newDeb=selfDeleted[1]
    newIns=selfDeleted[0]
    newTable=selfDeleted[2]
    selfList=selfDeleted[3]
    totalNodes=len(list(newTable.keys()))
    relations={}          #Kmer Strings are keys values are numbers of relations
    totalRelations=0
    for i in newTable.keys():
        relations[i]=newTable[i][0]+newTable[i][1]
        totalRelations+=(newTable[i][0]+newTable[i][1])
    hyperNodeCutoff= int(totalRelations/totalNodes)
    #for i in relations.copy().keys():
        #if relations[i]<=hyperNodeCutoff:
            #del relations[i]
    return [newDeb,relations,listOfRails]




from random import seed
from random import randint
from random import shuffle
from copy import deepcopy
import os
import pydot
from subprocess import check_call
from PIL import Image

deBruijn={}
answer=[]
seed(1)
def getkmers(seq, k):
    k_mers = []
    len1= len(seq)-k+1
    for i in range(len1):
        k_mers.append(seq[i:(i+k)])
    shuffle(k_mers)
    return k_mers
def DeBruijn(kmers):
    global deBruijn
    len1=len(kmers[0])-1
    for i in kmers:
        node= i[0:len1]
        outdegree=i[1:len1+1]
        if node not in deBruijn.keys():
            deBruijn[node]=[]
        deBruijn[node].append(outdegree)
    return
def indegrees(Deb):
    ind={} #dictionary of indegrees
    for i in Deb.keys():
        for o in Deb[i]:
            if o not in ind.keys():
                ind[o]=[]
            ind[o].append(i)
    return ind
def Table(Deb):
    out=Deb
    ind= indegrees(Deb)
    table={}
    for i in ind.keys():
        if i not in table.keys():
            table[i]=[]
        table[i].append(len(ind[i]))
    for i in out.keys():
        if i not in table.keys():
            table[i]=[0]                    #took me a while to add this 0 here!
        table[i].append(len(out[i]))
    for i in table.keys():
        if len(table[i])==1:
            table[i].append(0)
    return table    
def check1(table):
    diffhigh=0 
    diff_1=0
    diff1=0
    checkResult={"start":"","finish":"","isEulerian":False,"isCircuit":False}
    for i in table.keys():
        if (table[i][1] - table[i][0])==1:
            diff1+=1
            checkResult["start"]=i
        elif (table[i][1] - table[i][0])==-1:
            diff_1+=1
            checkResult["finish"]=i
        elif (table[i][1] - table[i][0])==0:
            pass
        else:
            diffhigh+=1
    if diffhigh == 0 and diff_1==0 and diff1==0:
        checkResult["isEulerian"]= True
        checkResult["isCircuit"]= True
    elif diff_1==1 and diff1==1 and diffhigh == 0:
        checkResult["isEulerian"]= True
        checkResult["isCircuit"]= False
    else:
        checkResult["start"]= ""
        checkResult["finish"]= ""
        checkResult["isEulerian"]= False
        checkResult["isCircuit"]= False
    return checkResult
def algorythm(deb,start):
    changingDeb= deb
    temp_path=[start]
    global answer
    motor1=True
    position=temp_path[-1]
    while motor1==True:
        if position not in changingDeb.keys():
            changingDeb[position]=[]
        optionCount=len(changingDeb[position])
        if optionCount > 0:
            choice= randint(1,optionCount)
            temp_path.append(changingDeb[position][choice-1])
            del changingDeb[position][choice-1]
            position=temp_path[-1]
        else:
            answer.insert(0,position)
            del temp_path[-1]
            if len(temp_path)>0:
                position=temp_path[-1]
            else:
                motor1=False
    return            
def program(list_of_kmers):     
    global answer 
    DeBruijn(list_of_kmers)           
    Deb=deepcopy(deBruijn)
    T=Table(Deb)    
    R=check1(T)
    if R["isEulerian"]==True and R["isCircuit"]==True:
        start=list(T)[randint(0,(len(list(T))-1))]  #just randomly picks a key
        algorythm(Deb,start)
    elif R["isEulerian"]==True and R["isCircuit"]==False:
        algorythm(Deb,R["start"])
    else:
        return
    seq=""
    K=len(list_of_kmers[0])
    for i in answer:
        seq+=i[0:1]  
    if R["isCircuit"]==False:
        seq+=answer[-1][-K+2:]
        note="Eulerian Path"
    elif R["isCircuit"]==True:
        seq=seq[0:-1]
        note="Eulerian Circuit"
    result=[note,seq]
    return result
def stringToList(string):
    output=string.split("', '")
    output[0]=output[0][2:]
    output[-1]=output[-1][0:-2]
    return output
def gifMaker():
    n= len(answer)
    for i in range(n):
        exec("file"+str(i)+" = open('dot"+str(i)+".dot','x')")
        exec("file"+str(i)+".close()")
        exec("file"+str(i)+" = open('dot"+str(i)+".dot','w')")
        strex=extraFunction(i)
        exec("file"+str(i)+".write(strex)")
    for i in range(n):
        exec("file"+str(i)+".close()")
    for i in range(n):
        exec("file"+str(i)+"=open('dot"+str(i)+".dot','r')")
        exec("fileP"+str(i)+"=open('pic"+str(i)+".png','x')")
        exec("fileP"+str(i)+".close()")
        exec("fileP"+str(i)+"=open('pic"+str(i)+".png','w')")
        exec("(graph,) = pydot.graph_from_dot_file('dot"+str(i)+".dot')")
        exec("graph.write_png('pic"+str(i)+".png')")
        exec("fileP"+str(i)+".close()")
    for i in range(n):
        exec("file"+str(i)+".close()")
        exec("os.remove('dot"+str(i)+".dot')")
    frames = []
    for i in range(n):
        exec("new_frame = Image.open('pic"+str(i)+".png')")
        exec("frames.append(new_frame)")
    frames[0].save('Path.gif', format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=300, loop=0)
    for i in range(n):
        exec("os.remove('pic"+str(i)+".png')")
    return
def extraFunction(i):
    strex="digraph G {\n"
    if i == len(answer)-1:
        for j in list(deBruijn.keys()):
            for f in deBruijn[j]:
                strex += '"'+j+'"'+' [color = black]\n'
                strex += '"'+f+'"'+' [color = black]\n'
                strex += '"'+j+'"'
                strex += " -> "
                strex += '"'+f+'"'+' [color = green]\n'                
    else:
        for j in list(deBruijn.keys()):
            for f in deBruijn[j]:
                if answer[i]==j and answer[i+1]==f:
                    strex += '"'+j+'"'+' [color = green]\n'
                    strex += '"'+f+'"'+' [color = green]\n'
                    strex += '"'+j+'"'
                    strex += " -> "
                    strex += '"'+f+'"'+' [color = red]\n'
                else:
                    strex += '"'+j+'"'
                    strex += " -> "
                    strex += '"'+f+'"'+'\n'
    strex += "}"
    return strex
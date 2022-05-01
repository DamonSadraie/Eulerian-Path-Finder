from random import seed
from random import randint
from random import shuffle
seed(1)
def getkmers(seq, k):
    k_mers = []
    len1= len(seq)-k+1
    for i in range(len1):
        k_mers.append(seq[i:(i+k)])
    shuffle(k_mers)
    return k_mers
def DeBruijn(kmers):
    deBruijn = {}
    len1=len(kmers[0])-1
    for i in kmers:
        node= i[0:len1]
        outdegree=i[1:len1+1]
        if node not in deBruijn.keys():
            deBruijn[node]=[]
        deBruijn[node].append(outdegree)
    return deBruijn
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
    answer=[]
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
    return answer           
def program(list_of_kmers):     
    print=""               
    Deb=DeBruijn(list_of_kmers)
    T=Table(Deb)    
    R=check1(T)
    if R["isEulerian"]==True and R["isCircuit"]==True:
        start=list(T)[randint(0,(len(list(T))-1))]  #just randomly picks a key
        answer=algorythm(Deb,start)
        #print("The Eulerian Circuit: ",answer)
        #print+= "The Eulerian Circuit: "+str(answer)+"\n"
    elif R["isEulerian"]==True and R["isCircuit"]==False:
        answer=algorythm(Deb,R["start"])
        #print("The Eulerian Path: ",answer)
        #print+= "The Eulerian Path: "+str(answer)+"\n"
    else:
        #print("Not Eulerian")
        print+="Not Eulerian"
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
    #print("The Sequence: ",seq) 
    result=[note,seq]
    return result
###################          Instructions:
#A="put your sequence in A"   #1-(starting with a sequence)    put your sequence in A
#B= getkmers(userinput,7)            #...                             change the number to set your K
#shuffle(B)                   #2-(starting with a Kmer list)   assign your list of Kmers to B
###################          End of Instructions

#program(B)                   #Run the code when ready
def stringToList(string):
    output=string.split("', '")
    output[0]=output[0][2:]
    output[-1]=output[-1][0:-2]
    return output


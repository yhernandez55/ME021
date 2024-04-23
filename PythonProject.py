MyFileName= 'TrigTable.txt'
# Each colum is ranging from angle to csc
# as of rught now errors
angle= [] # this is the angle values
sec = [] # Sec Values
tan= [] # Tan values
cot = [] # Cot val
sin= [] # Sin val
cos= [] # Cos val
csc= [] #Csc val
with open(MyFileName,'r') as DataFile:
    headers = DataFile.readline().split()
    for line in DataFile:
        valstrings=line.split()
        angle.append(float(valstrings[0]))
        sec.append(float(valstrings[1]))
        tan.append(float(valstrings[2]))
        cot.append(float(valstrings[3]))
        sin.append(float(valstrings[4]))
        cos.append(float(valstrings[5]))
        csc.append(float(valstrings[6]))

                    
import math
inf=math.inf
def helpcode(q,r):
    if (float(q)!=(float(r))) and (q==inf or r==inf):
        return inf
    if (float(q)!=0):
        return (abs(float(r)-float(q))/float(q))
    elif (float(r)!=0):
        return (abs(float(r)-float(q))/float(r))
    else: 
        return 0
for i in range(len(angle)):
    asin=('%.4f'%(sin[i]))
    acos=('%.4f'%(cos[i]))
    atan=('%.4f'%(tan[i]))
    acsc=('%.4f'%(csc[i]))
    asec=('%.4f'%(sec[i]))
    acot=('%.4f'%(cot[i]))
    #c=('%.4f'%(1/csc[i]))
    #b=('%.4f'%(1/sec[i])) 
    
    # comment correct output: csc(0), sin(18), sin(36), tan(66) four errors
   
    if (cos[i])!=0:
       btan=('%.4f' % (float(sin[i])/float(cos[i])))
    else:
        btan=inf
    if float(asec)!=0:
        bcot=('%.4f' % ((csc[i])/(sec)[i]))
    else: bcot=inf
    
    if helpcode(btan,tan[i])>0.01: #tan cos sin check
        if float(acsc)!=0:
            c=('%.4f'%(1/(float(acsc))))
        else:c=inf 
        if float(asec)!=0:    
            b=('%.4f'%(1/(float(asec))))
        else: b=inf 
    
        if helpcode(c,asin)>0.01: # yes statment     #(sin[i]==0) and (acsc!=0) and (abs(float(asin)-(float(bsin))<0.01)): 
            print('Incorrect value found:','sin(' +str(angle[i]) +')','was','%.4f' % sin[i],'instead of', c) 
            sin[i]=c
        elif helpcode(b,acos)>0.01: 
            print('Incorrect value found:','cos(' +str(angle[i]) +')','was','%.4f' % cos[i],'instead of', b) 
            cos[i]=b
        else: 
            print('Incorrect value found:','tan(' +str(angle[i]) +')','was','%.4f' % tan[i],'instead of', btan) 
            tan[i]=btan
           
    
    
    if helpcode(bcot,cot[i])>0.01: #cot csc sec check
        if float(acsc)!=0:
            if (angle[i])==0:
                c=acot
            else: c=('%.4f'%(1/(float(acsc))))
        else: c= inf
        
        if float(asec)!=0:    
            b=('%.4f'%(1/(float(asec))))
        else: b=inf
        if helpcode(c,acsc)>0.01: # yes statment     : 
            print('Incorrect value found:','cot(' +str(angle[i]) +')','was','%.4f' % csc[i],'instead of', c) 
            csc[i]=c
        elif helpcode(b,asec)>0.01: 
            print('Incorrect value found:','sec(' +str(angle[i]) +')','was','%.4f' % sec[i],'instead of', b) 
            sec[i]=b
        else: 
            print('Incorrect value found:','csc(' +str(angle[i]) +')','was','%.4f' % float(bcot),'instead of', cot[i]) 
            csc[i]=cot[i]
            
            


           
            
f=open('CorrectTrigtable.txt','w')
f.write('%12s %12s %12s %12s %12s %12s %12s\n'%('angle','sin','cos','tan',\
                                          'sec','csc','cot')) 
for i in range(len(angle)):
    f.write('%12d %12.4f %12.4f %12.4f %12.4f %12.4f %12.4f\n' % ((float(angle[i])),\
    (float(sin[i])),(float(cos[i])),(float(tan[i])),(float(sec[i])),(float(csc[i])),(float(cot[i]))))
f.close()
DataFile.close()

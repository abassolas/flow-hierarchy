import matplotlib
matplotlib.use("Agg")
import numpy as np
import math
import matplotlib.pyplot as plt
network={}
afile="network_file.csv"
with open(afile) as f:
      for index,line in enumerate(f):

	    terms = [term.strip() for term in line.split(";")]
	    conn=network.get(terms[0],"error")
	    if conn=="error":
		  network[terms[0]]={}
	    network[terms[0]][terms[1]]=float(terms[2])





ostr={}
istr={}
for source in network:
    for target in network[source]:
        if source!=target:
            conn=ostr.get(source,"error")
            if conn=="error":
                ostr[source]=0
            conn=istr.get(target,"error")

            if conn=="error":
                istr[target]=0
            istr[target]=istr[target]+network[source][target]
            ostr[source]=ostr[source]+network[source][target]

astr={}
if len(ostr)>2:

    b=0
    tot1=0


    while b==0:


        b=0
        if len(astr)==len(ostr):
			b=1
        if tot1>30:
			b=1
        if b==0:


            c1=len(astr)
            list1=[]

            for key1 in ostr:

                conn=astr.get(key1,"error")
                if conn=="error":
                    list1.append(ostr[key1])
            list2=sorted(list1)
            x=[]
            y=[]
            tot=0
            for index,element in enumerate(list2):

                y.append(tot/sum(list2))
                x.append(float(index)/float(len(list2)))
                tot=tot+element
            y.append(tot/sum(list2))
            x.append(float(index+1)/float(len(list2)))

            yn=[]
            xn=[]

            z=np.polyfit(x[-2:],y[-2:],1)
            for element in x:
                value=element*z[0]+z[1]
                yn.append(element*z[0]+z[1])
                xn.append(element)
            dx=-z[1]/z[0]


            for index,element in enumerate(list2):

                if float(index)/float(len(list2))<dx:
                    dw=element

       #     print dx
            for key in ostr:
                conn=astr.get(key,"error")

                if ostr[key]>=dw and conn=="error":
                    astr[key]=tot1
            if c1==len(astr):
                for key in ostr:
                    conn=astr.get(key,"error")
                    if conn=="error":
                        astr[key]=tot1
            print "threshold",dw
            print "Hotspot level",tot1
            print "Total nodes assigned",len(astr)
            tot1=tot1+1

#plt.legend()
#plt.ylim([0,1])
#plt.savefig("derivatives.pdf")
#plt.clf()

hnet={}
#print network["4875f79"]
for source in network:

    for target in network[source]:
        if source!=target:

            conn1=hnet.get(astr[source],"error")
            if conn1=="error":

                hnet[astr[source]]={}
   #         print astr[target]
            conn1=hnet[astr[source]].get(astr[target],"error")
            if conn1=="error":
                hnet[astr[source]][astr[target]]=0
            hnet[astr[source]][astr[target]]=hnet[astr[source]][astr[target]]+network[source][target]

suma=0
for key in hnet:
   for key1 in hnet[key]:
      suma=suma+hnet[key][key1]

traza=0
second=0
traza1=0
second1=0
total=0
for key in hnet:
    for key1 in hnet[key]:

        hnet[key][key1]=hnet[key][key1]/suma
        if key==key1:
            traza=traza+hnet[key][key1]
        if key==key1+1 or key==key1-1:
            second=second+hnet[key][key1]

flowh=traza+second
print "Phi",flowh

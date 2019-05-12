def rev(i):
   s1 = ''
   for c in i:
        s1 = c + s1  
   return s1
m=[int(i) for i in input().split()]
s=[]
ma=[]
for i in range(m[0]):
   l=input().split()
   s.append(l)
rlr=''
for i in range(m[0]):
   if(i%2==0):
      for j in s[i]:
         rlr=rlr+j
   else:
      r=[]
      for j in s[i]:
         r.insert(0,j)
      for k in r:
            rlr=rlr+rev(k)
ma.append(int(rlr))
lrl=''
lr=[]
for i in s:
   lr.insert(0,i)
for i in range(m[0]):
   if(i%2==1):
      for j in lr[i]:
            lrl=lrl+j
   else:
      r=[]
      for j in lr[i]:
         r.insert(0,j)
      for k in r:
         lrl=lrl+rev(k)
ma.append(int(lrl))
dud=''
du=[]
for i in range(m[1]):
   if(i%2==0):
      for j in range(m[0]):
         dud=dud+s[j][i]
   else:
      for j in range(m[0]-1,-1,-1):
         dud=dud+s[j][i]
ma.append(int(dud))
udu=''
ud=[]
for i in s:
   ud.insert(0,i)
for i in range(m[1]-1,-1,-1):
   if(i%2==0):
      for j in range(m[0]):
         udu=udu+rev(ud[j][i])
   else:
      for j in range(m[0]-1,-1,-1):
         udu=udu+rev(ud[j][i])
ma.append(int(udu))
print(max(ma))

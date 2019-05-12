n=int(input())
m=[]

for i in range(n):
   r=input()
   l=len(r)
   for i in range(l):
      if(r[i]=='0'):
         y=r[:i]
         p=r[i+1:]
         r=y+'o'+p
      if(r[i]=='1'):
         y=r[:i]
         p=r[i+1:]
         r=y+'l'+p
      if(r[i]=='2'):
         y=r[:i]
         p=r[i+1:]
         r=y+'z'+p
      if(r[i]=='5'):
         y=r[:i]
         p=r[i+1:]
         r=y+'s'+p       
   m.append(r)    
print(m)
r=int(input())
for i in range(r):
   s=input()
   sum=0
   for j in m:
      sum=sum+j.count(s)
   print(sum)

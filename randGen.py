import random
a=open("apiList",'r').read().split("\n")
s=a[random.randint(0,len(a)-1)].split(":")
t=a[random.randint(0,len(a)-1)].split(":")
f=a[random.randint(0,len(a)-1)].split(":")

print(f[1]+"\n with \n"+s[1]+"\n and \n"+t[1]+"\n via \n"+f[0]+" and "+s[0]+" and "+t[0]+"\ncategories: "+f[2]+" "+s[2]+" "+t[2])

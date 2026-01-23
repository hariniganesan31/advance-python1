'''n=1234
h=str(n)
print(h[::-1])

p=56789
m=str(p)
print(len(m))'''


k=[1,2,3,4,5]
s=0
for i in k:
    s+=i
print(s)

b=[1,2,3,4]
count=0
for i in b:
    count+=1
print(count)

n=[10,20,30,40,50]
key=int(input("enter"))
for i in n:
    if i==key:
        print("exits")
        break

t=(10,20,50,70)
for i in t:
  print(i)


d=[23,44,53,32]
print(tuple(d))

t={12,33,54,65}
t.add(23)
print(t)

r=[23,54,75,12,39,99]
print(max(r))

d1={"dept":"ai","domain":55}
c=0
s=d1.keys()
for i in s:
  c+=1
print(c)


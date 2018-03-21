a=[]
b=[]
for i in range(0,4):
    m=int(raw_input(" Enter value for a list :"))
    a.append(m)
for i in range(0,4):
    n=int(raw_input(" Enter value for b list :"))
    b.append(n)
for x in a:
  print(x,a.index(x))
for y in b:
  print(y,b.index(y))

I = []
t1 = 0
t2 = 1
n = 10
next_term = t1 + t2
while(next_term<=n):
  I.append(next_term)
  t1 = t2
  t2 = next_term
  next_term = t1 + t2
print I

time = float(input("Input time in minutes: "))
if (time<60):
  hour=0
  minutes=time
else:
  hour=time/60
  minutes=time%60
print("h:m-> %d %d" % (hour, minutes))

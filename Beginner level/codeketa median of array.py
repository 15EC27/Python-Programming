def median(lst):

    lst.sort()

    a = len(lst)

    if a % 2 == 0:
        b = lst[len(lst)/2]
        c = lst[(len(lst)/2)-1]
        d = (b + c) / 2
        return d

    if a % 2 > 0:
        return lst[len(lst)/2]

myList = []
n=input("Enter number of elements:")
for i in range(1,n+1):
    b=int(input("Enter element:"))
myList.append(b)
print(median(myList))

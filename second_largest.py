l = [3, 1, 4, 1, 5, 9, 2, 6]
if l[0] > l[1]:
    max1 = l[0]
    max2 = l[1]
else:
    max1 = l[1]
    max2 = l[0]
for i in range(2,len(l)):
    if l[i] > max1:
        max2 = max1
        max1 = l[i]
    elif l[i] > max2:
        max2 = l[i]
print(max2)
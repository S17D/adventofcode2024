
input = open("input.txt","r")
lst = input.readlines()

lst = [l.strip().split() for l in lst]

l1 = [int(l[0]) for l in lst]
l2 = [int(l[1]) for l in lst]
l1.sort()
l2.sort()
s = 0
for i in range(len(l1)):
    s += abs(l1[i]-l2[i])
print(s)

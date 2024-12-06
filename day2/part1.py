f = open("input.txt","r")
lst = [i.strip().split() for i in f.readlines()]

s = 0
for l in lst:
    ls = [int(o) for o in l]
    
    safe = True
    rev = None
    for i in range(len(ls)-1):
        if not ((ls == sorted(ls) or ls == sorted(ls,reverse=True)) and abs(ls[i]-ls[i+1]) in [1,2,3]):
            safe = False

        
    if safe:
        print(ls)
        s+=1
print(s) 
print()
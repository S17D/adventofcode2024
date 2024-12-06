f = open("input.txt","r")
lst = [i.strip().split() for i in f.readlines()]

def is_safe(ls):
    safe = True
    if not (ls == sorted(ls) or ls == sorted(ls,reverse=True)):
            return False
    for i in range(len(ls)-1):
        if not abs(ls[i]-ls[i+1]) in [1,2,3]:
            safe = False
            break
    return safe
s = 0
for l in lst:
    ls = [int(o) for o in l]
    safe = is_safe(ls)
    if not safe:
        for i,l in enumerate(ls):
            safe = is_safe([ls[j] for j in range(len(ls)) if j != i])
            if safe:
                break
        #print(f"{ls} is safe : {safe}")    
    if safe:
        s+=1
print(s) 

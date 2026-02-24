

nums = [3,2,4]
target = 6
mydict = {}
a = 0
out1=[]
for i in nums:
    print(i)
    mydict[i] = a
    a += 1
print(mydict)

for i in nums:
    out = target - i
    #print(out)
    if mydict[out]:
        out1.append(mydict[out])
        out1.append(mydict[i])
        break
print(out1)

    # if i - target in mydict:
        # print(mydict[i-target])
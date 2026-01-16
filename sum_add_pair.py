arr=[2,7,11,15]
tar=26
seen=set()
for i in arr:
    if tar-i in seen:
        print(i,tar-i)
        break
    seen.add(i)

arr=[1,2,3,4,5,5,6,6,6]
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
print(freq)
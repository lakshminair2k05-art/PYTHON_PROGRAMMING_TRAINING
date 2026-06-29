numbers=list(map(int,input('enter the list:').split()))
k=int(input('enter the threshold point'))
freq=dict()
for num in numbers:
    freq[num]=freq.get(num,0)+1#get func gets the key
for num,count in freq.items():#items gets the key and value pair
    if count>k:
        print(f"{num}:{count} times")

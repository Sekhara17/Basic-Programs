def bubbles(arr):
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    
bubs= [3,2,8,5,6,1]
bubbles(bubs)
print(bubs)
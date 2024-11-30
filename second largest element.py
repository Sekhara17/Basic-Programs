def lar(arr):
    max = 0
    s_max = 0
    count = 0
    for i in range(len(arr)):
        if arr[i]>max:
            s_max = max
        
            max = arr[i]
        elif arr[i] > s_max and arr[i]<max:
            s_max = arr[i]

    return s_max,count
arr = [2,1,5,5,5,7,9,12,11,11]
print(lar(arr))
def rotate(arr,d):
    res = arr[-d:] + arr[:-d]
    return res

arr = [int(i) for i in input().split()] 
d = 3
print(rotate(arr,d))
        
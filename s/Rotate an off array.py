def rotate_arr(arr,k):
    n = len(arr)
    tmp = [0] * n
    for i in range(n):
        tmp[(i + k) % n] = arr[i]
    return tmp
    
arr = list(map(int,input().split()))
k = int(input())
rotated_arr = rotate_arr(arr,k)
print(rotated_arr)
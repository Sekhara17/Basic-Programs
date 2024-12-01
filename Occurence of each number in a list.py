def occur_num(arr):
    arr1 = set(arr)
    for num in arr1:
        print(num,arr.count(num),sep =" --> ")

occur_num([1,5,3,4,5,2,1])
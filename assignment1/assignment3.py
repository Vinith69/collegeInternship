n = int(input("Enter the size of array\n"))
if 1 < n < 11:
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar-2])
else:
    print("n size must be between 2 and 10")

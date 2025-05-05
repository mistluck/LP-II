def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min], arr[i]
        print(f"Step:{i+1}{arr}")
    return arr

arr = [25,28,20,15,26]
print("Original Array",arr)
sorted = selection_sort(arr)
print("Sorted Array:",sorted)


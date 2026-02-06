class bubble_sort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    print("Sorted array is:", arr)

#li = int(input("Enter the number of elements in the array: "))
arr = [34,2,3,4,2,3,42,53,4]
# for i in range(li):
#     num = int(input("Enter element : "))
#     arr.append(num)
b = bubble_sort()
b.sort(arr)

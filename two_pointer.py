class two_pointer:
    def two_sum(self,arr,target):
        self.arr = arr
        left = 0
        right = len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                print("Pair found:", arr[left], arr[right])
                break
            elif current_sum < target:
                left += 1
            else:
                right -= 1

target = int(input("Enter the target sum: "))
li = 5
arr = []
for i in range(li):
    num = int(input("Enter element : "))
    arr.append(num)
tp = two_pointer()
tp.two_sum(arr,target)
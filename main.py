from random import randint

k = int(input())

nums = [randint(0, 20) for i in range(randint(k, k+20))]

print(nums)

def kbig(nums, k):
  while (k != 0):
    max_num = max(nums)
    nums.remove(max_num)
    k -= 1
  return max_num

print(kbig(nums, k))
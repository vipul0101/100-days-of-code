# HERE WE HAVE TO CREATE A FIBONACCI SERIES

def fib(nums):
  if nums in(0,1):
    return nums

  else:
    return fib(nums-1)+fib(nums-2)

fib = [fib(nums) for nums in range(9)]
print(fib)
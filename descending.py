print("Input six integers:")
nums = list(map(int, input().split())) 
nums.sort()
nums.reverse() 

print("After sorting the said ntegers:") 

print(*nums)

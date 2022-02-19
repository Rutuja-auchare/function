# write a phython programe to get sum of non-interger number
# test data:
# sumofdigit(345) -> 12
# sumdigits(45)
# -> 9
 
 def sumofdigits(n):
     if n==0:
         return 0
     else:
         return n%10+sumofdigits(int(n/10))
print(sumdigits(345))
print(sumdigits(45))    
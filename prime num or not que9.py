def number():
    n=int(input("enter the under:"))
    sum=0
    i=1
    while i<=n:
        if n%i==0:
            sum=sum+1
        i=i+1
    if sum==2:
        print("prime number",n)
    else:
        print("not prime number",n)
number()

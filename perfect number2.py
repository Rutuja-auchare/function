def perfect():
    a=int(input("enter the number:"))
    sum=0
    i=1
    while sum<a:
        if a%i==0:
            sum=sum+1
        i=i+1
    if a==sum:
        print("number is a perfect number:")
    else:
        print("is not perfect number")
perfect()        
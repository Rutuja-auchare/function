speed=int(input("enter the speed:"))
i=0
while i<=speed:
    if speed<=70:
        print("ok")
    elif speed>=70:
        i=0
        while i>=70:
            if speed==5:
                i=i+5
                print("i")
            i=i+1

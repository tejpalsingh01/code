n=int(input())
l=[]
while n>0:
    num=int(input())
    while num>0:
        rem=num%2
        l.append(str(rem))
        num=num//2
    l.reverse()
    print(("".join(l)).rjust(8,'0'))
    l=[]
    n=n-1


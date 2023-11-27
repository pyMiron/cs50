a=int(input())
b=int(input())


def evklid(a,b):
    while a!=b:
        if a>b:
            a=a-b
        elif a<b:
            b=b-a
        print(a,b)
    return a,b
print(evklid(a,b))
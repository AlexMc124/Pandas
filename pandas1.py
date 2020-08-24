def recursion(k):
    if k == 0:
        print("Recursion Over!")
        return 0
    else:
        print(k)
        recursion(k-1)


recursion(10)
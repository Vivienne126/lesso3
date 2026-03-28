#Space complexity 1
def sum(n):
    return n*(n+1)//2
print(f"Sum of first 5 numbers is {sum(5)}")


#Space complexity is n
def summ(n):
    if n<=0:
        return 0
    return n+summ(n-1)
print(f"Sum of first 5 numbers is {summ(5)}")

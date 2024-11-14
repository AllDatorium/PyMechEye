#function that uses a,b,c
#a is asked inside. b and c are arguments of the function
#check if a > 0. If yes, max(a, b, c). Otherwise return -1
def find(b, c):
    a = int(input("a = "))
    if a > 0:
        return(max(a, b, c))
    else:
        return -1
b = int(input("b = "))
c = int(input("c = "))
print("result is " + str(find(b, c)))

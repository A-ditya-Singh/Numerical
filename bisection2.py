print("x^3-x-11")
def f(x):
    return float(x**3 - x - 11)
lower =0.0
upper = 1.0
while (True):
    if(f(lower)*f(upper) < 0):
        break
    lower += 1.0
    upper += 1.0
print("",lower,upper)
i=1
while(True):
    print("\n")
    print("Itreation number:",i)
    i+=1
    mid = (lower + upper) / 2
    if(f(mid) < 0):
        lower = mid
    elif(f(mid) > 0):
        upper = mid
    print("New range",lower,upper)
    if(abs(f(mid)) < 0.001):
        break
print("Root is:", mid)
print(f(mid))
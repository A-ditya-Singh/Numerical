def f(x):
    return float(x**3 - x - 4)

def regula_falsi():
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
        mid = lower - (f(lower)*(upper-lower))/(f(upper)-f(lower))
        if(f(mid) < 0):
            lower = mid
        elif(f(mid) > 0):
            upper = mid
        print("New range",lower,upper)
        if(abs(f(mid)) < 0.001):
            break
    print("Root is:", mid)
    print(f(mid))
def main():
    print("Regula Falsi Method")
    regula_falsi()

if __name__ == "__main__":
    main()
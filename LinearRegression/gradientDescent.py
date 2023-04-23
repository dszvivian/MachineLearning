#Find Grdient Descent for x^2


def f(x):
    return x**2

def df(x):
    return 2*x


x=234; #initial guess
learing_rate = 0.1
precision = 0.001# Stopping Criteria
max_iter = 1000


for i in range(max_iter):
    previous_x =x
    x=x - (learing_rate*df(x))

    if(abs(x-previous_x)<precision):
        print(f"Converged after {i} iterations.")
        break
    else:
        pass



print("x=",x)








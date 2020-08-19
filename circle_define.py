def circle_area(r):
    yee = r**2*3.14
    return yee

def circle_circum(s):
    leo = s*3.14
    return leo

n = int(input("半徑"))
d = circle_area(n)

z = int(input("直徑"))
z = circle_circum(z)
 
print(d)
print(z)

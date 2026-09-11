# que 6 :triangle types 
x,y,z = map(int,input("enter three side of triangle ").split())
print( "three sides are ",x,y,z)
if x == y and y == z :
    print("equilateral triangle")
elif ( x == y or y == z  or z==x) :
    print("isoscale triangle")
else :
    print("scalane triangle")
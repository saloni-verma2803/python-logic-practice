# que 8 : discount system 
x = int(input("enter ammount : "))

if x >= 10000 :
    print("20 percent discount") 
     
    print("final amount after 20per discount : " ,x-(x*20/100))
elif x >= 5000 :
    print("10 percent discount") 
     
    print("final amount after 10per discount : " ,x-(x*10/100))
elif x < 5000 :
    print("no discount") 
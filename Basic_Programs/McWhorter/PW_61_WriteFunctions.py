'''
PW 61 writing functions
'''
def rectSolve(len,wid):
    #global area,perimeter,diagonal
    area=rectArea(len,wid)
    perimeter=rectPerimeter(len,wid)
    diagonal=rectDiagonal(len,wid)
    return area,perimeter,diagonal
 
def rectArea(len,wid):
    area=len*wid
    return area
 
def rectPerimeter(len,wid):
    perimeter=2*len+2*wid
    return perimeter
 
def rectDiagonal(len,wid):
    diag=(len**2+wid**2)**(1/2)
    return diag
   
while True:
    l=float(input("What is Length of your Rectangle? "))
    w=float(input("what is the Width of your Rectuangle? "))
    a,p,d = rectSolve(l,w)
    print("Your Rectangle Information: ")
    print("Area: ",a)
    print("Perimeter: ",p)
    print("Diagonal: ",d)
    print()
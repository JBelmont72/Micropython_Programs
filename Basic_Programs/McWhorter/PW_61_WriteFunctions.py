'''
PW 61 writing functions
also some of PW62 for high, low grades and sorting
'''
# def rectSolve(len,wid):
#     #global area,perimeter,diagonal
#     area=rectArea(len,wid)
#     perimeter=rectPerimeter(len,wid)
#     diagonal=rectDiagonal(len,wid)
#     return area,perimeter,diagonal
 
# def rectArea(len,wid):
#     area=len*wid
#     return area
 
# def rectPerimeter(len,wid):
#     perimeter=2*len+2*wid
#     return perimeter
 
# def rectDiagonal(len,wid):
#     diag=(len**2+wid**2)**(1/2)
#     return diag
   
# while True:
#     l=float(input("What is Length of your Rectangle? "))
#     w=float(input("what is the Width of your Rectuangle? "))
#     a,p,d = rectSolve(l,w)
#     print("Your Rectangle Information: ")
#     print("Area: ",a)
#     print("Perimeter: ",p)
#     print("Diagonal: ",d)
#     print()
  
def mainDef(ar):
    hi,lo=high_low_Grade(ar)
    array=sort_High_Low(ar)
    return hi,lo,myArray
def high_low_Grade(array):
    hg =0
    lg=100
    for i in range(len(array)):
        if hg < array[i]:
            hg = array[i]
        if lg >array[i]:
            lg =array[i]
    return hg,lg

def sort_High_Low(array):
    for j in range(0,len(array)-1,1):
        for i in range(0,len(array)-1-j,):## can subtract j since we know the j index becomes the highest each time trough, more efficient and faster 
        # for i in range(0,len(array)-1,1):
            if array[i]<array[i+1]:
                temp =array[i+1]
                array[i+1]=array[i]
                array[i]=temp
    return array        
myArray=[66,44,77,22]

# h,l =high_low_Grade(myArray)
# print(h, '  ',l)
# ar = sort_High_Low(myArray)
# print(ar)
h,l,newArray =mainDef(myArray)
print(h,l, newArray)
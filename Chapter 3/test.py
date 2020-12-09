def main():
    a = [10,5,8,7]
    n1= function1(a)
    print (n1, a[2])
    function2 (a)    
    print (a)

def function1(list1):
    x = list1[2] + list1[0]
    return x
    
def function2 (c):
     c[2] = 37
     c[1] = 67
   
main()

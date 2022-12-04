filename = "input.txt"
with open(filename) as file:
    
    counter = 0
    counterTaskTwo = 0
    for line in file:
        a,b = line.rstrip().split(",")
        a1,a2 = a.split("-")
        b1,b2 = b.split("-")
        #print("A1: ", a1, " A2: ", a2, " B1: ",b1," B2: ",b2 )
        
        if((int(a1)) >= int(b1)) and (int(a2) <= int(b2)):
            #print("A: ",a1,"-",a2," wchodzi w sklad B: ",b1,"-",b2)
            counter=counter+1
        elif((int(a1) <= int(b1)) and (int(a2) >= int(b2))):
            #print("B: ", b1,"-",b2," wchodzi kompletnie w sklad A: ",a1,"-",a2)
            counter=counter+1
        else:
            print("A1:",a1," A2:",a2," B1:",b1," B2:",b2)
        #print("Counter: ", counter)
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)    
        if (a2 < b1):
            print("doesn't overlap")
        elif(b2 < a1):
            print("doesn't overlap")
        else:
            counterTaskTwo=counterTaskTwo+1

    print("Overlapping areas count: ", counter)
    print("Overlapping total: ", counterTaskTwo)


# with open(filename) as file:
    
#     counter = 0
#     for line in file:
#         a,b = line.rstrip().split(",")
#         a1,a2 = a.split("-")
#         b1,b2 = b.split("-")
#         a1 = int(a1)
#         a2 = int(a2)
#         b1 = int(b1)
#         b2 = int(b2)

#         if (a2 < b1):
#             print("doesn't overlap")
#         elif(b2 < a1):
#             print("doesn't overlap")
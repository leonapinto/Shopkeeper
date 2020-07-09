#three modules imported:
import os
import datetime
import functools

# 4 functions defined:
def myfunc(list_1):
    for index,i in enumerate(list_1):                       #enumerate function
        if(list_1.index(i) !=0):
            print(index,i[0])
    name=int(input("Enter a choice:"))
    if(name<len(list_1)):                                     #length of lists
        print("1)Specification \n2)Availability \n3)Places Available \n4)Price \n5)Tax")
        requirement=int(input("Enter a choice:"))
        if(requirement==1):
            print("Specs:",list1[name][requirement])          #list indexing
        elif(requirement==2):
            print("Availability:",list1[name][requirement],"places")
        elif(requirement==3):
            print("Available in our stores in",list1[name][requirement])
        elif(requirement==4):
            print("Price:",list1[name][requirement])
        elif(requirement==5):
            print("Tax on the Electronic device:",list1[name][requirement])
    else:
        print("Invalid entry.")
        myfunc(list_1)
def addfunc(list_2):
    sumval=0
    for i in list_2:
            if(list_2.index(i) !=0):
                print(list_2.index(i),i[0])
    name=int(input("Enter a choice:"))
    mon=float(list_2[name][4])
    tax=(float(list_2[name][5]) / (100)) * mon
    val=mon + tax
    sumval+=val
    return sumval
def tryagain():
        print("                            Thank you for for your support!!")
        x=datetime.datetime.now()
        print("                                      ",x)
def add(x,y):
    return x+y

#open all the required text files acnd creating a list of the information inside:
with open('Television.txt','r') as television:
    list1=[]
    lines = television.readlines()
    for i in lines:
        list1.append(i.rstrip("\n").split(";"))             #appending lists
with open('laptop.txt','r') as Laptop:
    list2=[]
    lines = Laptop.readlines()
    for i in lines:
        list2.append(i.rstrip("\n").split(";"))
with open('Tablets.txt','r') as Tablets:
    list3=[]
    lines = Tablets.readlines()
    for i in lines:                                         #looping in lists
        list3.append(i.rstrip("\n").split(";"))
with open('Cell.txt','r') as Cell:
    list4=[]
    lines = Cell.readlines()
    for i in lines:
        list4.append(i.rstrip("\n").split(";"))
with open('Home_appliances.txt','r') as Home:
    list5=[]
    lines = Home.readlines()
    for i in lines:
        list5.append(i.rstrip("\n").split(";"))
with open('smart.txt','r') as smart:
    list6=[]
    lines = smart.readlines()
    for i in lines:
        list6.append(i.rstrip("\n").split(";"))
with open('headphones.txt','r') as headphones:
    list7=[]
    lines = headphones.readlines()
    for i in lines:
        list7.append(i.rstrip("\n").split(";"))
with open('camera.txt','r') as camera:
    list8=[]
    lines = camera.readlines()
    for i in lines:
        list8.append(i.rstrip("\n").split(";"))             #forms a nested list
with open('apple.txt','r') as apple:
    list9=[]
    lines = apple.readlines()
    for i in lines:
        list9.append(i.rstrip("\n").split(";"))
with open('watches.txt','r') as watch:
    list10=[]
    lines = watch.readlines()
    for i in lines:
        list10.append(i.rstrip("\n").split(";"))   

# Welcoming the user and asking for the necessary input:                    
print("We bring good things to life \nPlease choose any of the options below:")
start="y"
while(start=="y"):
    value=int(input("1)Checking\n2)Billing \n3)Increase/Decrease Tax: \n4)Check the net worth \nPlease enter a Choice:"))
    
    #if the user chooses "checking" the below code is executed:
    if(value==1):
        with open('inventory.txt','r') as inventory:
            for i in inventory:
                print(i)

        number=int(input("Enter a number:"))
        if(1<= number <=10):

            #To check Televisions
            if(number==1):
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list1)
                    cont=input("Do you like to check for another Television? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check Laptops/Computers        
            if(number==2):
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list2)
                    cont=input("Do you like to check for another Laptop/Computer? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check for Tablets:
            elif(number==3):  
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list3)
                    cont=input("Do you like to check for another Tablet? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check for Cell Phones:
            elif(number==4):   
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list4)
                    cont=input("Do you like to check for another Cell phone? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check for Home appliances
            elif(number==5):    
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list5)
                    cont=input("Do you like to check for another Home appliance? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            # To check for Smart appliances in the kitchen:
            elif(number==6):      
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list6)
                    cont=input("Do you like to check for another Smart appliance? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check for headphones/speakers
            elif(number==7): 
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list7)
                    cont=input("Do you like to check for another headphones? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check for camera or camcorders
            elif(number==8):     
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list8)
                    cont=input("Do you like to check for another camera? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check for an apple device
            elif(number==9):
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list9)
                    cont=input("Do you like to check for another apple device? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()

            #To check for smart watches and Fitness
            elif(number==10):
                
                cont="y"
                while(cont=="y" or cont=="Y"):
                    myfunc(list10)
                    cont=input("Do you like to check for another watch? y/n:")
                    if(cont=="n" or cont=="N"):
                        start=input("Would you like to start again? y/n:")
                        if(start=="n" or start=="N"):
                            break
                        elif(start=="y" or start=="Y"):
                            start="y"
                        else:
                            tryagain()
                    elif(cont=="y" or cont=="Y"):
                        cont="y"
                    else:
                        tryagain()
        else:
            break

    #If the user chooses to "bill" the following code will be executed:
    if(value==2):
        sum_of_values=0
        val="y"
        while(val=="y"):
            with open("inventory.txt","r") as inventory:
                for i in inventory:
                    print(i)
            number=int(input("Enter a number:"))
            if(1<= number <=10):

                #To bill one or more television:
                if(number==1):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list1)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another TV to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another item?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to  the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total cost to be paid:", sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:", sum_of_values)

                #to bill one or more laptops/PCs
                if(number==2):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list2)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another laptop to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another item?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total cost to be paid:", sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:", sum_of_values)

                #to bill one or more tablets/e-readers:
                if(number==3):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list3)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another tablet to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another item?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total cost to be paid:", sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)

                #to bill one or more cell phones:
                if(number==4):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list4)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another cell phone to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another item?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total cost to be paid:", sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)
                
                #to bill one or more Home appliances:
                if(number==5):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list5)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another Home appliance to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another item?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total amount to be paid:",sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)
                                
                #to bill one or more Smart Kitchen Appliances
                if(number==6):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list6)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another Smart Kitchen Appliance to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another item?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total amount to be paid:",sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)
                        
                #to bill one or more headphones/speakers:
                if(number==7):
                
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list7)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another headphone to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another item?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total amount to be paid:",sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)

                #to bill one or more camera/camcorders
                if(number==8):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list7)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another camera to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another device?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total amount to be paid:",sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)
                        
                #to bill one or more apple devices
                if(number==9):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list9)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another apple devices to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another device?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total amount to be paid:",sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)
                        
                #to bill one or more smart watches
                if(number==10):
                    cont="y"
                    while(cont=="y" or cont=="Y"):
                        sumval=addfunc(list10)
                        sum_of_values+=sumval
                        cont=input("Would you like to add another smart watch to cart? y/n:")
                        if(cont=="n" or cont=="N"):
                            val=input("Would you like to bill another device?")
                            if(val=="n" or val=="n"):
                                start=input("Would you like to go to the main menu? y/n:")
                                if(start=="n" or start=="N"):
                                    print("Total amount to be paid:",sum_of_values)
                                    break
                                elif(start=="y" or start=="Y"):
                                    start="y"
                                    print("Total amount to be paid:",sum_of_values)

    #if the user chooses to "increase/decrease the tax percent":
    if(value==3):
        with open("inventory.txt","r") as inventory:
            for i in inventory:
                print(i)
        number=int(input("Enter a number:"))
        if(1<= number <= 10):

            #To increase/decrease tax percent in television
            if(number==1):
                with open('Television.txt','r') as television:
                    list1=[]
                    lines = television.readlines()
                    for i in lines:
                        list1.append(i.rstrip("\n").rsplit(";",1))
                    list1.pop(0)                                            #popping in lists
                    temp_list=[float(list1[i][1]) for i in range(1,len(list1))]   
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]                    #list comprehension
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp:
                    temp.write("Television name; Size; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list1)-1):                         #range in lists
                        a=str(list1[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a)
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("television.txt")
                os.remove(dst)
                os.rename(src,dst)

            #to increase/decrease tax percent in Laptops/PCs
            if(number==2):
                with open('laptop.txt','r') as laptop:
                    list2=[]
                    lines = laptop.readlines()
                    for i in lines:
                        list2.append(i.rstrip("\n").rsplit(";",1))
                    list2.pop(0)
                    temp_list=[float(list2[i][1]) for i in range(1,len(list2))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp:
                    temp.write("Laptop name; Screen Size; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list2)-1):
                        a=str(list2[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a)
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("laptop.txt")
                os.remove(dst)
                os.rename(src,dst)

            #to inccrease/decrease tax percent in tablets
            if(number==3):
                with open('Tablets.txt','r') as tablets:
                    list3=[]
                    lines = tablets.readlines()
                    for i in lines:
                        list3.append(i.rstrip("\n").rsplit(";",1))
                    list3.pop(0)
                    temp_list=[float(list3[i][1]) for i in range(1,len(list3))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp:
                    temp.write("Tablet name; Screen size; Availbility; Places Available in; Price; Tax\n")
                    for i in range(0,len(list3)-1):
                        a=str(list3[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a)
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("Tablets.txt")
                os.remove(dst)
                os.rename(src,dst)

            #to increase/decrease tax percent in cell phones
            if(number==4):
                with open('Cell.txt','r') as cell:
                    list4=[]
                    lines = cell.readlines()
                    for i in lines:
                        list4.append(i.rstrip("\n").rsplit(";",1))
                    list4.pop(0)
                    temp_list=[float(list4[i][1]) for i in range(1,len(list4))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp:
                    temp.write("Cell Phone Name; Screen Size; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list4)-1):
                        a=str(list4[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a)
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("Cell.txt")
                os.remove(dst)
                os.rename(src,dst)
                
            #to iincrease/decrease tax percent in Home appliances
            if(number==5):
                with open('Home_Appliances.txt','r') as home:
                    list5=[]
                    lines = home.readlines()
                    for i in lines:
                        list5.append(i.rstrip("\n").rsplit(";",1))
                    list5.pop(0)
                    temp_list=[float(list5[i][1]) for i in range(1,len(list5))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp:
                    temp.write("Name; Size; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list5)-1):
                        a=str(list5[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a)
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("Home_Appliances.txt")
                os.remove(dst)
                os.rename(src,dst)
                
            #to increase/decrease tax perent in smart Kitchen appliances
            if(number==6):
                with open('smart.txt','r') as smart:
                    list6=[]
                    lines = smart.readlines()
                    for i in lines:
                        list6.append(i.rstrip("\n").rsplit(";",1))
                    list6.pop(0)
                    temp_list=[float(list6[i][1]) for i in range(1,len(list6))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp: 
                    temp.write("Smart Appliances; Size; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list6)-1):
                        a=str(list6[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a) 
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("smart.txt")
                os.remove(dst)
                os.rename(src,dst)
                
            #to increase/decrease tax percent in headphones
            if(number==7):
                with open('headphones.txt','r') as headphones:
                    list7=[]
                    lines = headphones.readlines()
                    for i in lines:
                        list7.append(i.rstrip("\n").rsplit(";",1))
                    list7.pop(0)
                    temp_list=[float(list7[i][1]) for i in range(1,len(list7))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp: 
                    temp.write("Name; Colour; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list7)-1):
                        a=str(list7[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a) 
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("headphones.txt")
                os.remove(dst)
                os.rename(src,dst)

            #to increase/decrease tax percent in cameras
            if(number==8):
                with open('camera.txt','r') as camera:
                    list8=[]
                    lines = headphones.readlines()
                    for i in lines:
                        list8.append(i.rstrip("\n").rsplit(";",1))
                    list8.pop(0)
                    temp_list=[float(list8[i][1]) for i in range(1,len(list8))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp: 
                    temp.write("Camera Name; Specs; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list8)-1):
                        a=str(list8[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a) 
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("camera.txt")
                os.remove(dst)
                os.rename(src,dst)

            #To increase or decrease tax percent in apple devices
            if(number==9):
                with open('apple.txt','r') as apple:
                    list9=[]
                    lines = apple.readlines()
                    for i in lines:
                        list9.append(i.rstrip("\n").rsplit(";",1))
                    list9.pop(0)
                    temp_list=[float(list9[i][1]) for i in range(1,len(list9))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp: 
                    temp.write("Name; Colour; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list9)-1):
                        a=str(list9[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a) 
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("apple.txt")
                os.remove(dst)
                os.rename(src,dst)

            #to increase/decrease tax percent in watches
            if(number==10):
                with open('watches.txt','r') as watches:
                    list10=[]
                    lines = watches.readlines()
                    for i in lines:
                        list10.append(i.rstrip("\n").rsplit(";",1))
                    list10.pop(0)
                    temp_list=[float(list10[i][1]) for i in range(1,len(list10))]
                    tax=float(input("Enter the value:"))
                    tax_in=int(input("1)Increase Tax \n2)Decrease Tax  \nPlease choose:"))
                    if(tax_in==1):
                        temp2=[i+tax for i in temp_list]
                        print("The value has been increased.")
                    elif(tax_in==2):
                        temp2=[i-tax for i in temp_list]
                        print("The value has been decreased.")
                with open("temporary.txt","w") as temp: 
                    temp.write("Watch name; Specification; Availability; Places Available in; Price; Tax\n")
                    for i in range(0,len(list10)-1):
                        a=str(list10[i][0]) + "; " + str(temp2[i]) + "\n"
                        temp.write(a) 
                src=os.path.abspath("temporary.txt")
                dst=os.path.abspath("watches.txt") 
                os.remove(dst)
                os.rename(src,dst)
            start=input("Would you like to start again?y/n:")
            if(start=="n" or start=="N"):
                break
        else:
            break
    
    #If the user chooses to calculate the net worth of the store, the code below will be executed:
    if(value==4):
        add_list=[]
        for i in range(1,len(list1)):
            a=int(list1[i][4]) * int(list1[i][2])
            add_list.append(a)
        for i in range(1,len(list2)):
            b=int(list2[i][4]) * int(list2[i][2])
            add_list.append(b)
        for i in range(1,len(list3)):
            c=int(list3[i][4]) * int(list3[i][2])
            add_list.append(c)
        for i in range(1,len(list4)):
            d=int(list4[i][4]) *int(list4[i][2])
            add_list.append(d)
        for i in range(1,len(list5)):
            e=int(list5[i][4]) * int(list5[i][2])
            add_list.append(e)
        for i in range(1,len(list6)):
            f=int(list6[i][4]) * int(list6[i][2])
            add_list.append(f)
        for i in range(1,len(list7)):
            g=int(list7[i][4]) * int(list7[i][2])
            add_list.append(g)
        for i in range(1,len(list8)):
            h=int(list8[i][4]) * int(list8[i][2])
            add_list.append(h)
        for i in range(1,len(list9)):
            j=int(list9[i][4]) * int(list9[i][2])
            add_list.append(int(list9[i][4]))
        for i in range(1,len(list10)):
            k=int(list10[i][4]) *int(list10[i][2])
            add_list.append(k)
        integer=functools.reduce(add, add_list)                 #reduce function
        print("******The total worth of the chain of shops is:",integer,"******")
print("                            Thank you for for your support!!")
x=datetime.datetime.now()
print("                                      ",x)
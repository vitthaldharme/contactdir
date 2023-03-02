'''
main file
===========
'''

def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0

    

def create_contact():
        fp=open('data.txt','a')
        n=input("enter name:")
        mn=input("enter mobile number:")
        res=validate_mob(mn)
        #print(res)
        if res==1:
            a,b=searchmob(mn)
            if b==1:
                print("number already exist")
            else:
                d=n+":"+mn+"\n"
                fp.write(d)
                fp.close()
                print("contact created successfully!!")
        else:

             print("plesase enter valid mobile number")

            

def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("===========contact directory=============")
    print()
    print(d)
    print("=========================================")

def searchname():
        print("Search Contact Number By Name")
        ns=input("Enter Name")
        fp=open('data.txt','r')
        data=fp.readlines()
        #print(data)
        flag=0
        for x in data:
            # print(x)
            l=x.split(":")
            # print(l)
            # print(l[0])
            if ns.upper()==l[0].upper():
                print(x)
                flag=1
        if flag==0:
            
            print("Contact Not Found")
    
        fp.close()



def searchmob(n):
           fp=open ('data.txt','r')
           data=fp.readlines()
           for x in data:
               l=x.split(":")
               if int(ms)==int(l[1]):
                   #print("contact found:")
                   #print(x)

                   return x,1
           else:
               
                   return '',0


        
print("welcome to contact directory consloe application:")
print()
while True:
    print()
    print("1.create contact")
    print("2.view contact")
    print("3.sech by name")
    print("4.serch bt mobile number")
    print("5.exit")
    ch=int(input("enter your choise"))

    if ch==1:
        create_contact()
        
    elif ch==2:
           display()
           
    elif ch==3:
           searchname()
    elif ch==4:
          ms=input("enter mobile number to br serched")

          a,b=searchmob(ms)
          #print(a)
          #print(b)
          if b==1:
              print("contact found:")
              print(a)
          else:
              print("not found")
          
    elif ch==5:
           break

    else:
        print("plese enter valid option!!!")


print("thank you for using application")
    
        

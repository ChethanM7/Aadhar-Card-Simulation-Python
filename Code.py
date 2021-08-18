import random
def generate():
    f=open("aadhar.txt",'r+')
    
    name=input("Name : ")
    fname=input("Father's name : ")
    mname=input("Mothers's name : ")
    mob=input("Mobile number : ")
    while(mob):
        if (len(mob)==10):
            mob=mob
            break
        else:
            print("invalid")
            del mob
            mob=input("Enter again : ")
    
    email=input("Email : ")
    while(email):
        if('@' in email and '.' in email):
            email=email
            break
        else:
            print("invalid")
            del email
            email=input("Enter again : ")
    
    dob=input("DOB (dd/mm/yyyy) : ")
    while(dob):
        if(dob[2]=='/' and dob[5]=='/' and len(dob)==10 and int(dob[0:2])<32 and int(dob[3:5])<13 and int(dob[6:10])<2019):
             dob=dob
             break
        else:
            print("invalid")
            del dob
            dob=input("Enter again : ")
    gen=input("Enter gender (M/F/O) : ")
    while(gen):
    
        if(gen=='M' or gen=='F' or gen=='O'):
            gen=gen
            break
        else:
            print("Invalid")
            del gen
            gen=input("Enter again : ")
        
    rand='500'
    numb=1001
    k=0
    for i in f:
        k=k+1
    if (k==0):
        ano=rand+str(numb)
    else:
        ano=rand+str(numb+k)
           

    
    f.write(ano+' '+name+' '+fname+' '+mob+' '+email+' '+dob+' '+gen+' ')
    print()
    print("ADDRESS DETAILS: ")
    dno=input("Door no : ")
    loc=input("Locality : ")
    city=input("City : ")
    pincode=input("Pincode : ")
    while(pincode):
        if(len(pincode)==6):
            pincode=pincode
            break
        else:
            print("invalid")
            del pincode
            pincode=input("enter pincode : ")
    st=input("State : ")
    pas=str(random.randrange(245,2435))
    
    f.write(dno+' '+loc+' '+city+' '+pincode+' '+st+' '+pas+' '+mname+' '+'\n')
    print("\n\n\nAadhar successfully generated\n")
    print("Your aadhar no. is : ",ano)
    print("Your password is   : ",pas)
    print()
    print()
    print("To complete the process of AADHAR generation, ","Pls visit the nearest enrollment center with the following documents:\n",sep='\n')
    print("1. 2 passport size photo\n"
          "2. Copy of enrollemnt form (available in this website).\n"
          "3. Address and age proof.\n")
    
    f.close()
    


    
def view():
    f=open("aadhar.txt",'r')
    us=input("\t\tEnter ur aadhar no. : ")
    ps=input("\t\tEnter ur password   : ")
    t=1
    for l in f:
        k=l.split(" ")
        
        if(us==k[0] and ps==k[12]):
           print("\n\n----------------------------------------------------------------------------------------\n")
           print("Name          :",k[1],"\tAadhar Number:",k[0])
           print("Fathers's name:",k[2])
           if(k[6]=='M'):
               print("Gender: Male")
           elif(k[6]=='F'):
               print("Gender: Female")
           else:
               print("Gender: Other")
           
           print("ADDRESS:","\n"," "+k[7],",",k[8])
           print(" ",k[9],",",k[10])
           print(" ",k[11],".")
           print("\n",'\t\t\t\t\t*******','\t\t\t\t\t*******','\t\t\t\t\t*******','\t\t\t\t\t*******','\t\t\t\t\t*******',sep='\n')
           print("----------------------------------------------------------------------------------------\n")
           t=1
           break
        else:
            t=0
    if(t==0):
        print("\n\n\t\tWrong credentials, contact admin office if u have forgot ur aadhar no. or password\n")

print("\t\tUNIQUE IDENTIFICATION AUTHORITY OF INDIA\n")
print("\t\twww.uidai.gov.in\n")

print()

print("\t1.Generate new aadhar \n")
print("\t2.View your e-enrollment form\n")
k=int(input("Enter your choice : "))


if(k==1):
    generate()
    print()
    ki=int(input("Enter 1 to view e-enrollment form "))
    if(ki==1):
        view()
    else:
        print("Thank you ")
    
elif(k==2):
    view()
else:
    print("Invalid, close the app and open again ")
    
   
    
   

list1=[]
def student_detail(**kwargs):
    list1.append(kwargs)
def display():
    for i in list1:
        print("="*50)
        print("\n")
        j=1
        for k in i:
            print(f"{j}.{k}:{i[k]}")
            j+=1
        print("="*50)
# student_detail(Name= "jai" ,address="Sanik vihar",Mob_no=8299127613,COurse="BCA",Pin_no="273015")
# student_detail(Name="arman",address="Sanik vihar",Mob_no=8594127613,COurse="MCA",Pin_no="273015")
# student_detail(Name="jahid",address="Sanik vihar",Mob_no=7299127613,COurse="BCA",Pin_no="273015")
# student_detail(Name="varun",address="Sanik vihar",Mob_no=9299127788,COurse="BCA",Pin_no="273015")
while True:
    i=int(input("enter numbwe 1. To add details,2.For Display,3.For exit"))
    if i ==1:
        name=input("enter Name: ")
        AD=input('enter ADDRESS: ')
        add=int(input("enter addhar number: "))
        Mobile_NO=int(input("enter Mobile number: "))
        course=input("ENTER COurse ")
        student_detail(Name=name,address=AD,Mob_no=Mobile_NO,Aadhar=add,Course=course)
    if i==2:
        display()
    if i==3:
        display()
        break
        




    

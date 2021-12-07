class student:
    def __init__(self):
        self.name = "name"
        self.age = "age"
        self.id = "id"
        self.major = "major"
        self.GPA = "GPA"

    def insert_student(self):
        f = open("add_student.txt", "a")

        self.name=input("enter your name ")
        self.age=input("enter age ")
        self.id=input("enter id ")
        self.major=input("enter major ")
        self.GPA=input("enter GPA ")

        f.write(self.name+"/"+self.age+"/"+self.id+"/"+self.major+"/"+self.GPA+ "\n")
        f.close()

    def display_data(self):
        read_obj=open("add_student.txt", "r")
        for line in read_obj:
                print(line)
        read_obj.close()

    def search_data(self):
        count=0
        idin=input("enter the id for search ")
        f=open("add_student.txt","r")
        for line in f :
            name,age,id,major,GPA=map(str,line.split('/'))
            if idin==id:
                count=1
                break
        if count==1:
             print(f'name {name} \nage {age} \nid {id} \nmajor {major}  \nGPA {GPA}')
        else:
            print("this id not found !!   \n ---------------------------\n ")
        f.close()
    '''
    def delete_data(self):
           idin=input("enter the id for search")
           f=open("add_std.txt","r")
           mylist=[]
           for line in f :

               # name, age, id, major, GPA=map(str,line.split('/'))
               if idin==id:
                   # print(f'name {name} \n id {id} \n  age {age} \n GPA {GPA}  \n major {major}')
                   continue
               else:
                   mylist.append(line)
                   print("this id not found !!")
           f.close()
           '''









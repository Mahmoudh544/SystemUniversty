class doctor:
    def __init__(self):
        self.name ="name"
        self.age ="age"
        self.department ="department"

    def insert_doctor(self):
       add_doc = open("add_doc.txt", "w")
       self.name = input("enter your name ")
       self.age = input("enter age ")
       self.department = input("enter department ")
       add_doc.write(self.name + "/" + self.age + "/" + self.department+"\n")
       add_doc.close()

    def display_data(self):
        read_obj=open("add_doc.txt", "r")
        for line in read_obj:
                print(line)
        read_obj.close()


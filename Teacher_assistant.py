class teach_assistant:
    def __init__(self):
        self.name = "name"
        self.age = "age"
        self.department =" department"

    def insert_teach_assistant(self):
        add_tec = open("add_teach_assistant.txt", "w")
        self.name = input("enter your name ")
        self.age = input("enter age ")
        self.department = input("enter department ")
        add_tec.write(self.name + "/" + self.age + "/" + self.department + "\n")
        add_tec.close()

    def display_data(self):
        read_obj=open("add_teach_assistant.txt", "r")
        for line in read_obj:
                print(line)
        read_obj.close()
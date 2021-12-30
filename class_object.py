class Person():
    def __init__(self,name,age,location):
        self.Name = name
        self.Age = age
        self.Location = location

    def per_info(self):
        print("NAME:",self.Name, "and", "AGE:",self.Age)

    def per_location(self):
        print("LOCATION: ", self.Location)


Person_object = Person("RAJU MIA", 22, "DHAKA")
Person_object.per_info()
Person_object.per_location()
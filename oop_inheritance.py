class Person():
    def __init__(self,name,age,location):
        self.Name = name
        self.Age = age
        self.Location = location

    def per_info(self):
        print("NAME:",self.Name, "and", "AGE:",self.Age)

    def per_location(self):
        print("LOCATION: ", self.Location)


class Person_choice(Person):
    def __init__(self,name,age,location,hobby,color):
        self.Name=name
        self.Age=age
        self.Location=location
        self.Hobby=hobby
        self.Color=color

    def per_hobby(self):
        print(self.Name, "Like:", self.Hobby)

    def per_color(self):
        print(self.Name, "like:", self.Color)


person_choice_object= Person_choice("ASIFE",22,"TANGAIL","TRAVEL","RED AND WHITE")

# Using parent class method in child class.per_into and per_location is parent class personal method.
#so, we can access parent clss method by child clss --that's call inheritance.
person_choice_object.per_info()
person_choice_object.per_location()

#per_hobe and per_color is personal child class method
person_choice_object.per_hobby()
person_choice_object.per_color()

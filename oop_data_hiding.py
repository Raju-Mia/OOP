class Person:
    def __init__(self):
        self.Name= "Raju"
        self.__Pasword = "secreate"

    def per_info(self):
        print("the name is:", self.Name)
        print("The password is: ", self.__Pasword)


Person_object = Person()
print(Person_object.Name) # we can access normal public data . But-
'''
print(Person_object.__Pasword)# we can not access any hiding data without any method. 
'''
Person_object.per_info() # access hiding data with using method

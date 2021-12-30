'''
Private methods are those methods that should neither be accessed outside the class nor by any base class.
'''
class Person:
    def job(self):
        print("THIS IS NORMAL TEXT")
    def __password(self):
        print("THIS IS PRIVATE MESSAGE---")

Person_object = Person()
Person_object.job()
Person_object._Person__password() # use _classname(_Person) for using private message access.
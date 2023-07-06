# create a class pet
class Pet:
# create constructor with data attribute of name , animal type, and age
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0
# create an attribute for set name
    def set_name(self):
        self.__name = str(input("What is the name of your pet?: "))
# create an attribute for animal type 
    def set_animal_type(self):
        self.__animal_type = str(input("My pet is a: "))
# create an attribute for age
# return name
    def get_name(self):
        return self.__name
# return animal type
    def get_animal_type(self):
        return self.__animal_type
# return age

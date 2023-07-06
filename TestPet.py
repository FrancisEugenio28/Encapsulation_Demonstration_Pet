from Pet import Pet
# create an object named Pet
my_pet = Pet()
# make the user input all the data attributes needed
my_pet.set_name()
my_pet.set_animal_type()
my_pet.set_age()
# return all the data attributes and print the output
print("\nPet's Name: ", my_pet.get_name(), "\nAnimal Type: ", my_pet.get_animal_type(), "\nPet's Age: ", my_pet.get_age())
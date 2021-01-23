
class Dog:
    
    animal_group = "Mammal"
    animal_type = "Dog"
    no_of_dogs = 0
    
    def __init__(self, name, breed, gender, age):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
        
        # No use case where 'no_of_dogs' is relevent for an instance.
        # 'no_of_dogs' can still be overwritten by an instance.
        Dog.no_of_dogs += 1
    
    def pet(self):
        print(self.name + ": Woof Woof!")
    
    def is_a(self):
        print(self.name + " is a " + self.animal_group)
        print(self.name + " is a " + self.animal_type)

dog1 = Dog('Mitt', 'Bulldog', 'Good Girl', 13)

dog2 = Dog('Hick', 'French Terrier', 'Good Boy', 7)


# __dict__ holds the class/object namespace
# Documentation : "A dictionary or other mapping object used to store an objects
# (writable) attributes"
print(dog1.__dict__)
print(dog2.__dict__)

print(Dog.__dict__)

dog1.animal_group = "Bird"

print(dog1.__dict__)
print(dog2.__dict__)

# Checks namespace for an object's 'animal_group' value before falling back to class value.
dog1.is_a()
dog2.is_a()
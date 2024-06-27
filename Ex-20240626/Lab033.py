class Dog:
    def __init__(self):
       self.name = None
       self.Age = None
       self.Breed = None
       self.name = input('Enter the name of the Dog:\n')
       self.Age =  int(input(f'Enter the Age of the Dog:\n'))
       self.Breed = input('Enter the Breed of the Dog:\n')

dog1 = Dog()
print(f'Name of the dog is: {dog1.name}')
print(f'Age of the dog is: {dog1.Age} years')
print(f'Breed of the dog is: {dog1.Breed}')
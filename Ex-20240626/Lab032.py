class Dog:
    def __init__(self, name, Age, Breed):
        self.name = name
        self.Age = Age
        self.Breed = Breed

    def sleep(self, name):
        print(f'Dog that is sleeping is : ', name)


dog2 = Dog("Chow", "1",'BullDog')
dog3 = Dog("Mow", "2",'Pug')

print(f'{dog2.name} of age {dog2.Age} years is of {dog2.Breed} breed')
print(f'{dog3.name} of age {dog3.Age} years is of {dog3.Breed} breed')

dog2.sleep(f'{dog2.name}')
dog3.sleep(f'{dog3.name}')

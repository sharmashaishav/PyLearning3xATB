class person:
    #Attributes
    name = None
    id=None
    age=None
    phone_number= None

    #Behavior
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def sleep(self,name):
        print("I am Sleeping",name)

Shaishav= person()
Shaishav.name ='Shaishav Sharma'
Shaishav.walk()

vanya=person()
vanya.name="Vanya Sharma"
vanya.talk()

class Dog:
    name = 'Tommy'
    id = None

    def sleep(self,name='Tuffy'):
        print("Name of the Sleeping dog is\n",name)


dog1 = Dog()
print(Dog().name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print("---------------------")

dog2 = Dog()
print(Dog().name)
dog2.name = "Mow"
print(dog2.name)
dog2.sleep()
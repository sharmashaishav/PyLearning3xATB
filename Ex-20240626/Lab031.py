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
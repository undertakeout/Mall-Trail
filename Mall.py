class Mall():
    '''represents one mall'''
    def __init__(self,name, numStores, floors, city, state, GoodParking):
        '''attributes:
                name: str representing the name of the mall
                numStores: int representing how many stores are in the mall
                city: str representing the city the mall is located in
                state: str representing the state the mall is located in
                floors: int representing the number of floors in a mall
                GoodParking: oddball attribute. Might remove later'''
        self.name = name
        self.numStores=numStores
        self.city = city
        self.state = state
        self.floors = floors
        self.GoodParking = GoodParking

    def whatItsCalled(self):
        '''returns the name of the mall as a str'''
        return self.name

    def howManyStores(self):
        '''return the number of stores in the mall as an int'''
        return self.numStores

    def whatCity(self):
        '''return the city of the mall as a str'''
        return self.city

    def whatState(self):
        '''return the state of the mall as a str'''
        return self.state

    def isParkingGood(self):
        '''return the parking opinion as a str'''
        return self.GoodParking

    def howManyFloors(self):
        '''return the number of floors in the mall as an int'''
        return self.floors

class Item():
    '''represents an item. Items may be used or may provide a passive effect.'''
    def __init__(self,name,description,weight):
        '''attributes:
            name: str representing the name of the mall
            description: str explaining what the item does, its weight, or if it is useless(adding later)
            weight: int representing how much does the item weighs (each character can only carry so much.)
            useless: bool, set to False for now.'''
        self.name= name
        self.description = description
        self.weight = weight
        self.useless = False

    def getName(self):
        '''returns the name of the item as a str'''
        return self.name

    def getDesc(self):
        '''returns the description of the item as a str'''
        return self. description
        
    def getWeight(self):
        '''returns the weight of the item as an int'''
        return self.weight
#to-do: create many instances of items
apple =Item('Apple','Tastes good.',0.5)
pear = Item('Pear' , 'Tastes good.', 0.5)
    

class Inventory():
    def __init__(self, bagType, weight, capacity):
        self.bagType= bagType
        self.capacity = capacity
        self.weight = weight
        self.items = [0]*capacity

    def getCapacity(self):
        return self.capacity

    def getWeight(self):
        return self.weight

    def displayItems(self):
        return self.items

    def addItem(self,item):
      
        if 0 in self.items:
            self.items[self.items.index(0)] = item.name
        else:
            print( 'Not Enough Space. Please throw away an item.')
    
    def deleteItem(self,item):
        if item.name in self.items:
            self.items[self.items.index(item.name)] = 0
        else:
            print("You don't have that item. Check your spelling and try again."      )      

Purse = Inventory('Purse', 5, 10)
Backpack =Inventory('Backpack',7,15)
Wallet = Inventory('Wallet',2,0)

class Person():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class NPC(Person):
    def __init__(self,name,description, phrases,location,somethingElseHere):
        super().__init__(name,description)
        self.phrases = phrases
        self.location = location
        self.somethingElseHere = somethingElseHere
    
    def getPhrase(self,x):
        return self.phrases[x]


IntlMall=Mall("International Mall",190,2,'Tampa','Florida',"Busy")
onWebsite = True
OnlineRobot = NPC('OnlineRobot','This robot can give you information about the mall you want to go to.',
                [("Hello, this is the " + IntlMall.whatItsCalled()  +  " Online Robot. I can give you information about the mall. " + '\n'
                "What do you want to know? Please select from the following options" + '\n' + 
                "Type exit to turn the computer off"),
                ('There are ' + str(IntlMall.howManyFloors()) + ' floors'),
                ('We are located in ' + IntlMall.whatCity()),
                ('We are located in ' + IntlMall.whatState()),
                ('There are currently ' + str(IntlMall.howManyStores()) + ' stores!'),
                ('Our parking lot is usually ' + IntlMall.isParkingGood())],'online',None)


while onWebsite:
    Response1=input('\n'+"1: How many floors are there?" + '\n'+
                    "2: What city are you located in?" + '\n' +
                    "3: What state are you located in?" + '\n' +
                    "4: How many stores are there?" + '\n' +
                    "5: Is the parking lot busy?  "  + '\n')

    try:
        if int(Response1) < len(OnlineRobot.phrases):
            print(OnlineRobot.getPhrase(int(Response1)))
        else:
            print ("Sorry, I don't understand. Please select from the following options: " + '\n')

    except ValueError:
        if Response1.lower() == 'exit':
            onWebsite = False
        else:
            print ("Sorry, I don't understand. Please select from the following options: " + '\n')
        





from Mall import Item

class Store():
    '''represents one store'''
    def __init__(self,name,products,location,hours,catalog):
        '''attributes
            name: str representing name of store
            products:str representing items the store sells
            location: int representing the floor the store is on
            hours: range function representing the store hours of operation (using military time)
            catalog: dict mapping items(string) to price(float)'''
        self.name = name
        self.products = products
        self.location = location
        self.hours = hours
        self.catalog=products

    def getStoreName(self):
        '''returns name of the store as a str'''
        return self.name

    def getStoreProduct(self):
        '''returns the products the store sells as a str'''
        return self.products

    def getStoreLocation(self):
        '''returns the floor the store is on as an int'''
        return self.location

    def getHours(self):
        '''returns range of hours of operation in military time'''
        return self.hours

    def getStoreCatalog(self):
        '''returns a mapping of items to prices as a dict'''
        return self.catalog

item=Item('NULL','NULL',1)

AbFit=Store('Abercrombie & Fitch',
            'Clothing Store',
            1,
            range(11,19),
            {item:1.00})

Apple=Store('Apple',
            "Tech store",
            1,
            range(13,17),
            {item:1.00})

AnnTay=Store('Ann Taylor',
            "Clothing Store",
            1,
            range(11,19),
            {item:1.00})

Fabl=Store('Fabletics',
            'Athletic Clothing Store',
            1,
            range(11,19),
            {item:1.00})

Godiv=Store('Godiva',
            'Chocolatier',
            1,
            range(12,19),
            {item:1.00})

HelzBg=Store('Helzberg Diamonds',
            'Jewelry Store',
            1,
            range(12,18),
            {item:1.00})

JCrew= Store('J. Crew',
            'Clothing Store',
            1,
            range(11,18),
            {item:1.00})

Lush=Store('Lush',
          'Cosmetics Store',
          1,
          range(11,19),
          {item:1.00}  )


TSt=[Apple,AbFit,AnnTay,Fabl,Godiv,HelzBg,JCrew,Lush]
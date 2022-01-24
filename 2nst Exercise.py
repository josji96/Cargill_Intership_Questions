
class   Client:
    #constructor of the class "Cliente"
    def __init__(self, ID, Name, Address1, Address2, Town, Country, PostCode, Region, OuterPostCode, CountryID, Type, Since, CreditWorthy, IsDealer):
        self.ID = ID
        self.Name = Name
        self.Address1 = Address1
        self.Address2 = Address2
        self.Town = Town
        self.Country = Country
        self.PostCode= PostCode
        self.Region = Region
        self.OuterPostCode = OuterPostCode
        self.CountryID = CountryID
        self.Type = Type
        self.Since =  Since
        self.CreditWorthy = CreditWorthy
        self.IsDealer = IsDealer

class   Country_name(Client):
    #Constructor of the subclass "Country_Name"
    def __init__(self, ID, Name, Address1, Address2, Town, Country, PostCode, Region, OuterPostCode, CountryID, Type, Since, CreditWorthy, IsDealer, CountryName, CountryISOCode):
        super().__init__(ID, Name, Address1, Address2, Town, Country, PostCode, Region, OuterPostCode, CountryID, Type, Since, CreditWorthy, IsDealer)
        self.CountryName = CountryName
        self.CountryISOCode = CountryISOCode

class   Vehicle:
    #Constructor of the class "Vehicle"
    def __init__(self,Make, Model, ColorID, Type, CostPrice, Spareparts, LaborCost, Registration_Date, Mileage, PurchaseDate, AgeInYears):
        self.Make = Make
        self.Model = Model
        self.ColorID = ColorID
        self.Type = Type
        self.CostPrice = CostPrice
        self.Spareparts =  Spareparts
        self.LaborCost = LaborCost
        self.Registration_Date = Registration_Date
        self.Mileage = Mileage
        self.PurchaseDate = PurchaseDate
        self.AgeInYears = AgeInYears

class Color(Vehicle):
    #Constructor of the subclass " Color"
    def __init__(self, ColorID, Type, CostPrice, Spareparts, LaborCost, Registration_Date, Mileage, PurchaseDate, AgeInYears, color_name):
        super().__init__(ColorID, Type, CostPrice, Spareparts, LaborCost, Registration_Date, Mileage, PurchaseDate, AgeInYears)
        self.color_name = color_name
class Invoice:
    #Constructor of the class "Invoice"
    def __init__(self, InvoiceID, InvoiceNumber, ClientID, InvoiceDate, TotalDiscount, DeliveryCharge, InvoiceDateKey):
        self.InvoiceID = InvoiceID
        self.InvoiceNumber = InvoiceNumber
        self.ClientID = ClientID
        self.InvoiceDate = InvoiceDate
        self.TotalDiscount = TotalDiscount
        self.DeliveryCharge = DeliveryCharge
        self.InvoiceDateKey = InvoiceDateKey

    #Metodos 
    def Show_invoice_info(self):
        print("The invoice "+str(self.InvoiceID)+" with number "+str(self.InvoiceNumber)+"was sold to the client with ID number"+str(self.ClientID))
    def Show_charge(self):
        print("The delivery charge was "+str(self.DeliveryCharge))
    def Show_discount(self):
        print("The total discount was " +str(self.TotalDiscount))
#another type of vehicle
class truck():
    def __init__(self, Make, Model, ColorID, Age, RegistrationDate, Truck_class, duty_classification, weight_limit, Mileage):
        self.Make = Make
        self.Model = Model
        self.ColorID = ColorID
        self.Age = Age
        self.RegistrationDate = RegistrationDate
        self.Truck_class = Truck_class
        self.duty_classification = duty_classification
        self.weight_limit = weight_limit
        self.Mileage = Mileage
    def Show_specs(self):
        print("The truck of brand " + str(self.Make)+" and model " + str(self.Model)+" has the following specs" )
        print("Class{}".format(str(self.Truck_class)))
        print("A classification of {}".format(str(self.duty_classification)))
        print("And also a total weight limit of {}".format(str(self.weight_limit)))

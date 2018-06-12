class Product(object):
    def __init__(self, item_name, weight, brand, price):
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.price = price
        self.display_info()
        
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
            return self.price * (1 + tax)
    
    def return_reason(self, reason):
        #return_reason = None
        if reason.lower() == "defective":
            self.price = 0
            self.status = "defective"
        elif reason.lower() == "like new":
            self.status = "for sale"
        elif reason.lower() == "open":
            self.status = "used"
            self.price = price * 0.10
        return self

    def display_info(self):
        print "Item: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)
        print "Price: " + str(self.price)
        return self

product1 = Product("speakers", "3 lbs", "Bose", 50)
print product1.add_tax(0.12)  
product1.sell()
product1.display_info()
product1.return_reason("like new")
product1.dispaly_info()


#product1.sell()
#product1.add_tax()
#product1.dispaly_info()
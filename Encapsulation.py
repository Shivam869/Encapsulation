class computer:
    def __init__(self):
        self.__maxprice=900
    def __init__(self):
        print("Selling price: {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price
c= computer()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(1000)
c.sell()
        
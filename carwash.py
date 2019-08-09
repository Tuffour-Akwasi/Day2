
class Car_wash():
    def __init__(self, customer_name, car_id, car_name, car_type, car_color):
        self.customer_name = customer_name
        self.car_id = car_id
        self.car_name = car_name
        self.car_type = car_type
        self.car_color = car_color

    def customer_info(self):
        print("Customer Name: {}\n Car ID: {}\n Car Name: {}\n Car Type: {}\n Car Color: {}\n".format(self.customer_name,self.car_id,self.car_name,self.car_type,self.car_color))

    def customers(self):
        print(" Name: {} Id: {}".format(self.customer_name,self.car_id))

    def car_info(self):
        a = input("car id")
        a == self.car_id
        if a:
            print(" Car Name: {}\n Type {}\n Color {}".format(self.car_name,self.car_type,self.car_color))


    def message(self,sms,email,pa):
        pass


    def history(self,x):
        for x in customer_info:
            print(x)

p = Car_wash("Frank", 1001, "bmw", "saloon", "red")
p2 = Car_wash("Frank", 1001, "bmw", "saloon", "red")
p3 = Car_wash("Frank", 1001, "bmw", "saloon", "red")


Car_wash.history()

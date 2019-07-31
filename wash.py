class wash:
    def __init__(self,start_date, wash_day,customer_name,car_name,car_type,car_id,car_color):
        self.customer_name = customer_name
        self.car_name = car_name
        self.car_type = car_type
        self.car_id = car_id
        self.car_color = car_color
        self.start_date = start_date
        self.wash_day = wash_day

    def car_info(self):
        print("Car ID: {}\nCustomer name: {}\nStart Date: {}\nDay car was wash: {}".format(self.car_id,self.customer_name,self.start_date,self.wash_day))

    def car_charges():
        amount = 30
        print("To wash car you will be charge:",amount)

class customer(wash):

    def cus_info(self):
        pin = self.car_id
        pin = int(input("Enter car ID to check Your Information: "))
        if pin == self.car_id:
            print("customer name: {}\n car type: {}\n car type: {}\n car id: {}\n car color: {}".format(self.customer_name,self.car_name,self.car_type,self.car_id,self.car_color))
        else:
            print("please check id and type again")

p = customer("12/04/19","Tusday","Frank","BMW","Saloon",10001,"Red")
p2 =customer("12/04/19","Tusday","emma","BMW","Saloon",10002,"Red")
p3 = customer("12/04/19","Tusday","grace","BMW","Saloon",10003,"Red")


if __name__ == '__main__':
    p.customer.cus_info() 

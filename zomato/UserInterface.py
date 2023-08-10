class Dish:
    def __init__(self, dish_id, name, price, availability="no"):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.availability = availability
        self.sales_count = 0

class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = []
        self.status = 'preparing'



class Zomato:

    def __init__(self):
        self.menu = {}

    def add_dish_menu(self,dish_id,name,price,availability):
        dish = Dish(dish_id,name,price,availability)
        self.menu[dish_id] = dish
        print("Dish is Successfully Add to menu")

    def remove_dish(self,dish_id):
        del self.menu[dish_id]
        print("Dish is Successfully deleted from menu")

    def update_availability(self,dish_id,availability):
        if dish_id in self.menu:
            self.menu[dish_id].availability = availability
            print("Dish availability updated Successfully")
        else:
            print("Dish with this Id:", dish_id, "not found")

    def get_dish_by_id(self,dish_id):
        if dish_id in self.menu:
            return self.menu[dish_id]



    def display_menu(self):
        print("\nMenu:")
        for dish in self.menu.values():
            if dish.availability == "yes":
                print(f"{dish.dish_id}. {dish.name} - ${dish.price} ({availability})")


    orders = []

    def take_order(self, dish_ids, customer_name):
        order_id = len(self.orders) + 1
        new_order = Order(order_id,customer_name)

        dish = self.get_dish_by_id(dish_ids)
        if dish and dish.availability == "yes":
                new_order.dishes.append(dish)
        else:
            print(f"Dish with ID {dish_id} is not available.")
            return

        self.orders.append(new_order)
        print(f"Order {new_order.order_id} has been placed for {customer_name}.")

    def update_status_order(self,order_id,status):
        isFound = False
        for i in self.orders:
            if i.order_id == order_id:
                i.status = status
                isFound = True

        if isFound == False:
            print("Order with this id not Found :- ",order_id)


    def display_orders(self):
        print("All Orders:")
        for i in self.orders:
            print(f"Order ID: {i.order_id}, Customer: {i.customer_name}, Status: {i.status}")


    def review_order(self,order_id):
        for order in self.orders:
            if order.order_id == order_id:
                print(f"Order ID: {order.order_id}")
                print(f"Customer: {order.customer_name}")
                print("Dishes:")
                for dish in order.dishes:
                    print(f"  {dish.name} - ${dish.price}")
                print(f"Status: {order.status}")
                return
        print("Order not found.")







zomato = Zomato()

while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")
    print("1. Add Dish to Menu")
    print("2. Remove Dish from Menu")
    print("3. Update Dish Availability")
    print("4. Take Order")
    print("5. Update Order Status")
    print("6. Display Orders")
    print("7. Review Order")
    print("8. Display all menu items")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dish_id = int(input("Enter Dish ID: "))
        name = input("Enter Dish Name: ")
        price = float(input("Enter Dish Price: "))
        availability = input("Enter Dish Availability (yes/no): ")
        zomato.add_dish_menu(dish_id, name, price, availability)

    elif choice == 2:
        dish_id = int(input("Enter Dish ID to remove: "))
        zomato.remove_dish(dish_id)
    elif choice == 3:
        dish_id = int(input("Enter Dish ID: "))
        availability = input("Enter Dish Availability (yes/no): ")
        zomato.update_availability(dish_id,availability)
    elif choice == 4:
        dish_id = int(input("Enter Dish ID: "))
        customer_name = input("Enter the Customer Name:- ")
        zomato.take_order(dish_id,customer_name)
    elif choice == 5:
        dish_id = int(input("Enter Dish ID: "))
        availability = input("Enter Order Status: (Preparing,cooked,on your way,Delivered)")
        zomato.update_status_order(dish_id,availability)
    elif choice == 6:
        zomato.display_orders()
    elif choice == 7:
        dish_id = int(input("Enter Order ID: "))
        zomato.review_order(dish_id)
    elif choice == 8:
        zomato.display_menu()
    elif choice == 0:
        print("Exiting the Zomato Chronicles!")
        break

    else:
        print("Invalid choice. Please select a valid option.")







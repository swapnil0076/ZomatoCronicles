from django.shortcuts import render, redirect
from .forms import AddDishForm
from .forms import TakeOrderForm


class Dish:
    def __init__(self, dish_id, name, price, availability="no"):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.availability = availability


class Zomato:
    def __init__(self):
        self.menu = {}


zom = Zomato()


def add_dish_view(request):
    if request.method == 'POST':
        form = AddDishForm(request.POST)
        if form.is_valid():
            dish_id = form.cleaned_data['dish_id']
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            availability = form.cleaned_data['availability']

            # Create an instance of the Dish class
            dish = Dish(dish_id, name, price, availability)

            # Store the dish in the zomato's menu dictionary
            zom.menu[dish_id] = dish
            dishes = zom.menu.values()
            return render(request, "display_dishes.html", {"dishes": dishes})
    else:
        form = AddDishForm()
    return render(request, "add_dish_form.html", {'form': form})

def get_dish_by_id(dish_id):
    if dish_id in zom.menu:
        return zom.menu[dish_id]

def display_dishes(request):
    dishes = zom.menu.values()
    dish = get_dish_by_id(1)
    print(dish)
    return render(request, "display_dishes.html", {"dishes": dishes})


def update_availability(request):
    if request.method == 'POST':
        key_to_update = int(request.POST.get('key_to_update'))
        attribute = request.POST.get('attribute')
        new_value = request.POST.get('new_value')
        print("Debug:", zom.menu.values())
        print("Debug:", key_to_update, attribute, new_value)
        print("Debug: zom.menu keys =", zom.menu.keys())
        print("Debug: key_to_update =", key_to_update)
        print(zom.menu[key_to_update])
        if key_to_update in zom.menu:
            print("Debug:", "yes")
            dish = zom.menu[key_to_update]
            if attribute == 'name':
                dish.name = new_value
            elif attribute == 'availability':
                dish.availability = new_value
            elif attribute == 'price':
                dish.price = new_value
            return render(request, 'update_dish_avil.html', {'keys': zom.menu.keys()})
        else:
            # Dish not found, handle the error
            error_message = f"Dish with ID {key_to_update} not found"
            return render(request, 'update_dish_avil.html', {'keys': zom.menu.keys(), 'error_message': error_message})

    # Handle GET request or other cases
    return render(request, 'update_dish_avil.html', {'keys': zom.menu.keys()})


def delete_dish(request):
    if request.method == 'POST':
        dish_id = int(request.POST.get('dish_id'))
        if dish_id in zom.menu:
            del zom.menu[dish_id]
            return redirect('delete_dish')  # Redirect to the same page
        else:
            error_message = f"Dish with ID {dish_id} not found"
            return render(request, 'delete_dish.html', {'dish_ids': zom.menu.keys(), 'error_message': error_message})
    else:
        return render(request, 'delete_dish.html', {'dish_ids': zom.menu.keys()})



order_list = []
def take_order_view(request):
    menu_items = []

    for dish in zom.menu.values():
        if dish.availability == True:
            menu_items.append(dish)
    # dishes = zom.menu.values()
    print(menu_items)
    # order_list = []

    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('items')
        customer_name = request.POST.get('customer_name')
        quantities = request.POST.get('quantities', '').split(',')

        selected_items = [zom.menu[int(item_id)] for item_id in selected_item_ids]

        if selected_items and len(selected_items) == len(quantities):
            order = {
                'order_id': len(order_list) + 1,
                'customer_name': customer_name,
                'dishes': [],
            }
            for item, quantity in zip(selected_items, quantities):
                order['dishes'].extend([item] * int(quantity))
            order_list.append(order)
            message = f"Order {order['order_id']} has been placed for {customer_name}."
        else:
            message = "Invalid input or quantities"
    else:
        message = None

    context = {
        'menu_items': menu_items,
        'message': message,
    }
    print(order_list)

    return render(request, 'take_order.html', context)


def display_orders(request):
    return render(request, 'display_orders.html', {'orders': order_list})
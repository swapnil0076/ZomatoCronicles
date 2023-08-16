from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddDishForm
from .models import Dish, Order


#
# class Dish:
#     def __init__(self, dish_id, name, price, description, availability="no"):
#         self.dish_id = dish_id
#         self.name = name
#         self.price = price
#         self.description = description
#         self.availability = availability
#
#
# class Zomato:
#     def __init__(self):
#         self.menu = {}


# zom = Zomato()


def add_dish_view(request):
    if request.method == 'POST':
        form = AddDishForm(request.POST)
        if form.is_valid():
            dish_id = form.cleaned_data['dish_id']
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            availability = form.cleaned_data['availability']
            description = form.cleaned_data['description']

            # Create an instance of the Dish class
            dish = Dish(dish_id, name, price, availability, description)
            dish.save()
            # Store the dish in the zomato's menu dictionary
            # zom.menu[dish_id] = dish
            # dishes = zom.menu.values()
            return render(request, "display_dishes.html", {"dishes": form})
    else:
        form = AddDishForm()
    return render(request, "add_dish_form.html", {'form': form})


def get_dish_by_id(dish_id):
    try:
        dish = Dish.objects.get(pk=dish_id)
        return dish
    except Dish.DoesNotExist:
        return None


def display_dishes(request):
    dishes = Dish.objects.all()
    print(dishes)
    return render(request, "display_dishes.html", {"dishes": dishes})


def update_availability(request):
    if request.method == 'POST':
        key_to_update = int(request.POST.get('key_to_update'))
        attribute = request.POST.get('attribute')
        new_value = request.POST.get('new_value')

        try:
            dish = Dish.objects.get(dish_id=key_to_update)  # Fetch the dish from the database
        except Dish.DoesNotExist:
            error_message = f"Dish with ID {key_to_update} not found"
            return render(request, 'update_dish_avil.html', {'error_message': error_message})

        # Update the corresponding field in the Dish model
        if attribute == 'name':
            dish.name = new_value
        elif attribute == 'availability':
            dish.availability = new_value
        elif attribute == 'price':
            dish.price = new_value
        dish.save()

        return render(request, 'update_dish_avil.html', {'keys': Dish.objects.values_list('dish_id', flat=True)})

    # Handle GET request or other cases
    return render(request, 'update_dish_avil.html', {'keys': Dish.objects.values_list('dish_id', flat=True)})


#
#
def delete_dish(request):
    if request.method == 'POST':
        dish_id = int(request.POST.get('dish_id'))

        try:
            dish_to_delete = Dish.objects.get(dish_id=dish_id)  # Fetch the dish from the database
            dish_to_delete.delete()  # Delete the dish from the database
            return redirect('delete_dish')  # Redirect to the same page
        except Dish.DoesNotExist:
            error_message = f"Dish with ID {dish_id} not found"
            return render(request, 'delete_dish.html',
                          {'dish_ids': Dish.objects.values_list('dish_id', flat=True), 'error_message': error_message})
    else:
        return render(request, 'delete_dish.html', {'dish_ids': Dish.objects.values_list('dish_id', flat=True)})


def take_order_view(request):
    menu_items = Dish.objects.filter(availability=True)

    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('items')
        customer_name = request.POST.get('customer_name')
        quantities = request.POST.get('quantities', '').split(',')

        selected_items = Dish.objects.filter(dish_id__in=selected_item_ids)

        if selected_items and len(selected_items) == len(quantities):
            order = Order.objects.create(customer_name=customer_name, order_status='preparing')
            for item, quantity in zip(selected_items, quantities):
                order.dishes.add(item, through_defaults={'quantity': int(quantity)})
            message = f"Order has been placed for {customer_name}."
        else:
            message = "Invalid input or quantities"
    else:
        message = None

    context = {
        'menu_items': menu_items,
        'message': message,
    }

    return render(request, 'take_order.html', context)

def display_orders(request):
    orders = Order.objects.all()  # Retrieve all orders from the database
    return render(request, 'display_orders.html', {'orders': orders})


def update_order_status(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('new_status')

        try:
            order_to_update = Order.objects.get(id=order_id)
            order_to_update.order_status = new_status
            order_to_update.save()
        except Order.DoesNotExist:
            return HttpResponse('Invalid order ID')

    return redirect('display_orders')

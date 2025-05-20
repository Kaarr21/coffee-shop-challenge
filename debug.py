from coffee import Coffee
from customer import Customer
from order import Order

def main():
    # Create coffee instances
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    
    # Create customer instances
    nancy = Customer("Nancy")
    peter = Customer("Peter")
    charles = Customer("Charles")
    
    # Create orders
    order1 = nancy.create_order(espresso, 3.5)
    order2 = peter.create_order(latte, 4.0)
    order3 = peter.create_order(espresso, 3.5)
    order4 = charles.create_order(cappuccino, 4.5)
    order5 = nancy.create_order(latte, 4.0)
    
    # Test relationship methods
    print(f"Nancy's orders: {len(nancy.orders())}")
    print(f"Peter's coffees: {[coffee.name for coffee in peter.coffees()]}")
    print(f"Espresso orders count: {espresso.num_orders()}")
    print(f"Latte average price: ${latte.average_price():.2f}")
    print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")
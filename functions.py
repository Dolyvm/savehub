import time
import random


def generate_unique_order_number():
    current_time = int(time.time())
    random_number = random.randint(1, 10000)
    order_number = f"{current_time}{random_number}"
    return order_number




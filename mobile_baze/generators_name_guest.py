import random


def generate_guest_name():
    return f"Guest{random.randint(100000, 999999)}"
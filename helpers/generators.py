from faker import Faker
from random import randint, choice
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

fake = Faker("en_US")


def generate_bun_name():
    return f'{fake.name().lower()} bun'


def generate_price():
    return randint(10, 800)


def generate_ingredient_type():
    return choice([INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])


def generate_ingredient_name():
    return f'{fake.name().lower()} ingredient'


def generate_bun_data():
    return generate_bun_name(), generate_price()


def generate_ingredient_data():
    return generate_ingredient_type(), generate_ingredient_name(), generate_price()

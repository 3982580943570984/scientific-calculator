from dearpygui import dearpygui as dpg
from constants import *


def add_digit(sender, data, user_data):
    widget = user_data[0]
    number = int(dpg.get_value(widget))
    if number == 0:
        dpg.set_value(widget, user_data[1])
    elif number > 0:
        dpg.set_value(widget, number * 10 + user_data[1])
    else:
        dpg.set_value(widget, number * 10 - user_data[1])


def delete_last_digit(sender, data, user_data):
    widget = user_data
    number = int(dpg.get_value(widget))
    if number >= 0:
        dpg.set_value(widget, number // 10)
    else:
        dpg.set_value(widget, number // 10 + 1)


def clear_all(sender, data, user_data):
    widget = user_data
    dpg.set_value(widget, 0)


def clear_entry(sender, data, user_data):
    widget = user_data
    dpg.set_value(widget, 0)


def make_negative(sender, data, user_data):
    widget = user_data
    number = int(dpg.get_value(user_data))
    dpg.set_value(widget, -int(number))


def make_inverse(sender, data, user_data):
    widget = user_data
    number = float(dpg.get_value(widget))
    if number > 1:
        dpg.set_value(widget, float(1.0 / number))
    elif number > 0:
        dpg.set_value(widget, int(1.0 / number))


def make_pow(sender, data, user_data):
    widget = user_data
    number = int(dpg.get_value(widget))
    dpg.set_value(widget, int(pow(number, 2)))


def make_sqrt(sender, data, user_data):
    print()


def add_floating_point(sender, data, user_data):
    """Добавить точку"""
    print()


def add_arithmetic(sender, data, user_data):
    """Записать операцию в вычисление"""
    print()


def compute_value(sender, data, user_data):
    """Вычислить значение в вычислении"""
    print()

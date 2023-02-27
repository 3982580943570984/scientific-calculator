from dearpygui import dearpygui as dpg
from utilities import *
from constants import *


dpg.create_context()
dpg.setup_dearpygui()
dpg.create_viewport(title='Calculator', width=SCREEN_WIDTH,
                    height=550, x_pos=DISPLAY_CENTER_X, y_pos=DISPLAY_CENTER_Y,
                    small_icon='./icons/llvm.ico', large_icon='./icons/llvm.ico')


with dpg.window(tag='Primary', width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
                min_size=[300, 350], pos=[0, 0], no_close=True, no_move=True,
                no_collapse=True, no_title_bar=True) as main_window:

    compute_widget = dpg.add_input_text(
        tag='Compute', width=SCREEN_WIDTH - 32, default_value='', readonly=True)
    number_widget = dpg.add_input_text(
        tag='Entry', width=SCREEN_WIDTH - 32, default_value='0', scientific=True)

    # dpg.add_item_clicked_handler -
    # Добавить графу - точность вычисления

    with dpg.group(horizontal=True):
        dpg.add_button(label='%', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_arithmetic, user_data=[number_widget, '%'])
        dpg.add_button(label='CE', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=clear_entry, user_data=number_widget)
        dpg.add_button(label='C', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=clear_all, user_data=number_widget)
        dpg.add_button(label='DEL', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=delete_last_digit, user_data=number_widget)

    with dpg.group(horizontal=True):
        dpg.add_button(label='1/x', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=make_inverse, user_data=number_widget)
        dpg.add_button(label='x^2', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=make_pow, user_data=number_widget)
        dpg.add_button(label='sqrt(x)', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=make_sqrt, user_data=number_widget)
        dpg.add_button(label='/', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_arithmetic, user_data=number_widget)

    with dpg.group(horizontal=True):
        dpg.add_button(label='7', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 7])
        dpg.add_button(label='8', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 8])
        dpg.add_button(label='9', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 9])
        dpg.add_button(label='*', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_arithmetic, user_data=[number_widget, '*'])

    with dpg.group(horizontal=True):
        dpg.add_button(label='4', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 4])
        dpg.add_button(label='5', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 5])
        dpg.add_button(label='6', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 6])
        dpg.add_button(label='-', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_arithmetic, user_data=[number_widget, '-'])

    with dpg.group(horizontal=True):
        dpg.add_button(label='1', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 1])
        dpg.add_button(label='2', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 2])
        dpg.add_button(label='3', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 3])
        dpg.add_button(label='+', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_arithmetic, user_data=[number_widget, '+'])

    with dpg.group(horizontal=True):
        dpg.add_button(label='+/-', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=make_negative, user_data=number_widget)
        dpg.add_button(label='0', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_digit, user_data=[number_widget, 0])
        dpg.add_button(label='.', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=add_floating_point, user_data=[number_widget, '.'])
        dpg.add_button(label='=', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                       callback=compute_value, user_data=[number_widget, '='])


dpg.show_viewport()
dpg.set_primary_window('Primary', True)
dpg.start_dearpygui()
dpg.destroy_context()

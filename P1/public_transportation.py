import os
import platform
from dependency_injection import *

os_platform = platform.system()
CLEAR_COMMAND = 'cls' if os_platform == 'Windows' else 'clear'
queue = []

def print_objects(begin_label, end_label, separating_line_length, objects):
    print(begin_label)
    print('-' * separating_line_length, '\n')
    i = 0
    for i in range(len(objects)):
        print(i + 1, end='. ')
        objects[i].print_name()
    print(f'\n{end_label}')

def choose_object():
    os.system(CLEAR_COMMAND)
    print_objects('Выберите объект', '0. Завершить работу', 5, objects)
    
    obj_index = int(input()) - 1
    if obj_index != -1:
        print_object_info(objects[obj_index])
    else:
        os.system(CLEAR_COMMAND)
        print('Работа завершена')
        return

def print_object_info(object):
    global queue

    os.system(CLEAR_COMMAND)
    object.print_attributes()
    print_objects('\nСвязи', '0. Обратно', 3, object.relations)

    obj_index = int(input()) - 1
    if obj_index != -1:
        queue.append(object)
        print_object_info(object.relations[obj_index])
    elif len(queue) > 0:
        last_element = queue.pop()
        print_object_info(last_element)
    else:
        choose_object()

def launch():
    try:
        choose_object()
    except Exception as e:
        print('\nРабота завершена с ошибкой:', e)

launch()
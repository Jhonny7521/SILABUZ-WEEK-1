
def search_number(my_lsit):
    if user_input in (my_list):
        my_list.remove(user_input)
        return my_list
    else:
        result = f"{user_input} No existe en la lista"
        return result

my_list = [15, 20, 50, 80, 40, 60]
user_input = int(input('Ingrese un número de la lista: '))
print(search_number(my_list))

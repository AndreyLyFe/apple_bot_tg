
def phrase_for_start_first_greeting(data):
    return "Hello, " + data["user_name"] + "!"

def phrase_for_answer_to_main_menu_buttons(data):
    return "You pressed " + data["button_title"]
def answer_for_to_main_menu_one_button(data):
    return 'Вы перешли в ' + '"' + data['name_button'] + '"'

def answer_exit_to_main_menu():
    return 'Вы вернулись в главное меню'


#Будущая ветка для iphone.
# def show_iphone():
#     return 'Выберите интересующую Вас модель'
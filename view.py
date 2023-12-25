from note_operation import *
def view():
    print('Выберите действие: \n1 - прочитать заметки, \n2 - добавить и сохранить заметку, \n3 - редактировать заметку, \n4 - удалить заметку, \n5 - выход, \n6 - очистить форму')
    choice = input()
    if choice.isdigit: 
        if 0 < int (choice) < 7 :  
            match int(choice):
                case 1:
                    read_note()
                    
                case 2:
                    add_note()
                    
                case 3:
                    edit_note()
                    
                case 4:   
                    delete_note()
                    
                case 5:
                    print('Увидимся снова!')
                case 6:
                    init_note()
                
    else:
        print('Введите число от 1 до 6')
        view()
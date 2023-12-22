import datetime

def view():
    print('Выберите действие: \n1 - прочитать заметки, \n2 - добавить и сохранить заметку, \n3 - редактировать заметку, \n4 - удалить заметку, \n5 - выход')
    choice = input()
    if choice.isdigit: 
        if 0 < int (choice) < 6 :  
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
                
    else:
        print('Введите число от 1 до 5')
        view()



def get_id():
    print('получаем ID заметки')


def read_note(notes):
    print('Ваши заметки:')
    with open ('note.csv', 'r', encoding="utf-8") as note:
        for line in note:
            ar = line.split(';')
            date = ar [2]


            print(date)
            print(line)


def add_note(notes):
    if notes:
        last_id = notes[-1]['id']
    else:
        last_id = 0
    print('Добавление заметки')
    title = str(input('Введите заголовок: '))
    body = str(input('Введите текст заметки: '))
    time = str(datetime.datetime.now())
    note = {
            'id': last_id + 1,
            'title': title,
            'body': body,
            'times': time
        }
    notes.append(note)
    
    # with open ('note.csv', 'a', encoding="utf-8") as note:
       
    #     # count = note.
    #     note.write(note_m)
    #     note.write(time)
    #     note.write("\n")
    #     note.close
    print('Заметка "',title,'" успешно сохранена')

def edit_note(notes):
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Замените заголовок заметки: ")
            body = input("Замените текст заметки: ")
            note['title'] = title
            note['body'] = body
            note['time'] = datetime.datetime.now()
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")
    
def delete_note(notes):
    print("Удаление заметок")
    print("Ознакомьтесь со всеми заметками и выберите номер той, которую хотите удалить")
    read_note()
    del_num = input("Введите номер заметки, которую удалить:")
    if del_num.isdigit() and int(del_num) > 0:
        return del_num
    else:
        print('Введите целое положительное число!')

    with open ('note.csv', 'r', encoding="utf-8") as note:
        note = note.read()
        note_lines = note.split('\n')
        del_note_lines = note_lines.pop[del_num]
        print(del_note_lines)



print('Заметки')
view()


        

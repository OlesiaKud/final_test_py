import datetime
import csv

def init_note():
    # метод удаляет все записи, записывает 
    print('Обновляем список заметок')
    with open ('note.csv', 'w', encoding="utf-8", newline="") as note: 
        last_id = 0
        title = 'заголовок'
        body = 'текст заметки'
        time = 'дата'
      
        writer = csv.writer(note, delimiter=";")
        writer.writerow(
            [
                last_id,
                title,
                body,
                time
            ]
        )   

def get_id():
    try:
        with open('note.csv', 'r',encoding="utf-8", newline='') as file:
            reader = csv.DictReader(file)
            last_id = 0
            for row in reader:
                last_id = row[0]
            return last_id
    except FileNotFoundError:
        return 0
    

def read_note():
    print('Ваши заметки:')  
    with open ('note.csv', 'r', encoding="utf-8", newline="") as note:
        for line in note:
            print(line)


def add_note():
    with open ('note.csv', 'a', encoding="utf-8", newline="") as note: 
        n = get_id() + 1
        last_id = str(n)     
        print('Добавление заметки')
        title = str(input('Введите заголовок: '))
        body = str(input('Введите текст заметки: '))
        time = str(datetime.datetime.now())
      
        writer = csv.writer(note, delimiter=";")
        writer.writerow(
            (
                last_id,
                title,
                body,
                time
            )
        )   
    print('Заметка "',title,'" успешно сохранена')



def edit_note():
    read_note()
    note_id = input("Введите ID заметки для редактирования: ")
    if note_id.isdigit() and int(note_id) > 0:
        with open('note.csv', 'r', encoding="utf-8") as file:
            notes = list(csv.reader(file))
        
        if int(note_id) <= len(notes):
            del_note = notes.pop(int(note_id))
            with open('note.csv', 'w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(notes)
            last_id = note_id
            title = str(input('новый заголовок: '))
            body = str(input('новый текст: '))
            time = str(datetime.datetime.now())
         
            with open('note.csv', 'a', encoding="utf-8", newline="") as note:       
                writer = csv.writer(note, delimiter=";")            
                writer.writerow(
                    (
                    last_id,
                    title,
                    body,
                    time
                )
            )
            print('Заметка отредактирована')
        else:
            print('Заметки с таким id не существует!')
            

    
def delete_note():
    print("Удаление заметок")
    print("Ознакомьтесь со всеми заметками и выберите id той, которую хотите удалить")
    read_note()

    del_num = input("Введите номер заметки, которую удалить: ")
    if del_num.isdigit() and int(del_num) > 0:
        with open('note.csv', 'r', encoding="utf-8") as file:
            notes = list(csv.reader(file))
        
        if int(del_num) <= len(notes):
            del_note = notes.pop(int(del_num))
            with open('note.csv', 'w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(notes)
            print(f"Заметка с id {del_num} удалена: {del_note}")
        else:
            print('Заметки с таким id не существует!')
    else:
        print('Введите целое положительное число!')

user_choice = -1

tasks = ["Posprzątać śmieci", "Wynieść biurko"]

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "["+str(task_index)+ "]")
        task_index += 1

def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")      
    
def delete_task():
    task_index = int(input("Podaj indeks zadania do usunięcia: "))
    if (task_index < 0 or task_index > len(tasks) - 1):
        print("Nie ma takiego zadania")
        return
    else:
        tasks.pop(task_index)
    print("Usunięto zadanie!")

def save_task():
    file = open("tasks.txt" , "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()

def load_tasks():
    try:
        file = open("tasks.txt")
        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

load_tasks()

while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()
    
    if user_choice == 4:
        save_task()


    print()
    print("1. Pokaż zadanie")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")


    user_choice = int(input("Wybierz liczbę: "))
    print()

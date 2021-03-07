print("Колобок отправился путешествовать")
print("Встретил Медведя")
print("Убежать от медведя - 1")
print("Медведь съел хлеб - 2")

flag = False
while not flag: 
    go1 = int(input("Введите 1 или 2"));
    if go1 == 1:
        print("Встретил лису")
        flag = True
    elif go1 == 2:
        print("Медведь съел хлеб. Конец игры")
        flag = True
    else:
        print("Фигня")
        

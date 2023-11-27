try:
    with open('venv/text.txt','r',encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("файл не найден")

import shutil
import time
import os

query = input("Что ищем?\n>> ")

prompt = """Введите сколько часов назад был создан файл (примерно),
или пустой ввод если любой временной промежуток.
>> """

time_stamp = int(input(prompt) or 0) * 3600
time_now = time.time()
path = "/home/"
matches = []

for address, dirs, files in os.walk(path):

    for file in files:
        if query in file:
            full_path = os.path.join(address, file)

            if os.path.islink(full_path):
                continue

            if time_stamp:
                if time_now - os.path.getctime(full_path) < time_stamp:
                    matches.append(full_path)

            else:
                matches.append(full_path)



if not matches:
    print("Файл не найден.")

else:
    destination = input("Куда копировать?\n>> ")
    print(f"Копирую файлы в {destination}")

    for file in matches:

        file_name = file.split(os.path.sep)[-1]
        dst_file_name = os.path.join(destination, file_name)

        count = 2
        while os.path.exists(dst_file_name):

            dst_file_name = os.path.join(destination, file_name.replace(".", f"({count}).", count=1))

            count +=1
        

        shutil.copy2(file, dst_file_name)


shutil.make_archive("/home/pyhs/Рабочий стол/dst_backup", 'zip', destination)

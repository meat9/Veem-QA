import hashlib


def create_sum(dict_files):
    # Очистка файла перед подсчетом хеш сумм
    error = ''
    open("result.txt", "w").close()
    # Итерируемся по парам ключ:значение в словаре
    for k, v in dict_files.items():
        try:
            # Определяем алгоритм хеширования по значению ключа и вычисляем хеш
            hash = eval("hashlib." + v + "()")
            with open(k, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash.update(chunk)
            result3 = hash.digest()
            # Записываем результаты в файл в виде: файл тип хеш
            with open("result.txt", "a") as f:
                f.write(k + ' ' + v + ' ' + str(result3) + '\n')
        except Exception as e:
            error += str(e)
    if error != '':
        return "Generating checksum done with errors: " + error
    return "Generating checksum done"


def verify(dict_files):
    # Очистка файла перед подсчетом хеш сумм
    test = ''
    open("result_verify.txt", "w").close()
    # Итерируемся по парам ключ:значение в словаре
    for k, v in dict_files.items():
        try:
            # Определяем алгоритм хеширования по значению ключа и вычисляем хеш файлов
            hash = eval("hashlib." + v + "()")
            with open(k, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash.update(chunk)
            new_hash = str(hash.digest())
            #Читаем документ со списокм хеш-сумм
            with open("result.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    file = line.split(" ")[0]
                    #Если хеш создан для файла из документа - делаем сравнение
                    if file == k:
                        hash_from_file = line.split(" ", 2)[2].strip('\n')
                        #Записываем результаты проверки хеш-сумм
                        if hash_from_file == new_hash:
                            test = (k + ' ' + v + ' ' + 'OK' + '\n')
                        else:
                            test += (k + ' ' + v + ' ' + 'FAIL' + '\n')
                    else:
                        pass
        except Exception as e:
            #Если файл не найден - записывам ошибку
            test += (k + ' ' + v + ' ' + 'NOT FOUND' + '\n')
        with open("result_verify.txt", "a") as f:
            f.write(test)


#Функция create_sum создаст документ со списком файлов и хеш суммами (файлы берутся из словаря dict_files)
#Функция verify проверит данные из документа с хеш суммами (файлы берутся из словаря dict_files)
dict_files = {'quest5ion1.py': 'md5', 'question2.py': 'md5'}

print(create_sum(dict_files))
verify(dict_files)

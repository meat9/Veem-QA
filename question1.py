from os import path
import shutil
import xml.etree.ElementTree as ET


def main(xml):
    # Читаем файл xml
    mytree = ET.parse(xml)
    myroot = mytree.getroot()
    # Итерируемся по атрибутам xml
    for x in myroot:
        # Находим название файла и пути копирования (откуда и куда)
        _from_dir = x.attrib['source_path']
        _file = x.attrib['file_name']
        _to_dir = x.attrib['destination_path']
        # Если xml ориентирован под windows - заменим слеши
        slash_check = (_from_dir.find('/', 0))
        if slash_check == -1:
            slash = '\\'
        else:
            slash = '/'
        # Создадим полные пути для копирования файла
        copy_to = x.attrib['destination_path']+slash+_file
        copy_from = _from_dir+slash+_file
        # Проверим существование путей и файла
        test_file = path.exists(copy_from)
        test_folder = path.exists(_to_dir)
        if test_file == True and test_folder == True:
            # Если пути существуют - попробуем скопировать файл, если произойдет ошибка - функция вернет код ошибки
            try:
                shutil.copy2(copy_from, copy_to)
            except Exception as e:
                return e
        else:
            # Если путь и/или файл не существуют - выведем сообщение
            return "File %s or directory %s not exist, please check it. Or you don't have access to the file or directory" % (
                copy_from, _to_dir)


xml = ('question1_conf.xml')

if __name__ == "__main__":
    print(main(xml))

# Veem-QA

QA Automation Engineer

Задания для самостоятельного выполнения
Выберите одну любую задачу из представленных ниже. Решите задачу, написав код на одном из следующих языков:
    • Python
    • C/C++
    • C#
Рекомендуется там, где это уместно, использовать стандартные библиотеки, а не выполнять реализацию общеизвестных алгоритмов с нуля.


Задача 1
Реализовать программу, осуществляющую копирование файлов в соответствии с конфигурационным файлом. Конфигурационный файл должен иметь формат xml. Для каждого файла в конфигурационном файле должно быть указано его имя, исходный путь и путь, по которому файл требуется скопировать.

Пример
Конфигурационный файл:

<config>
    <file
            source_path="C:\Windows\system32"
            destination_path="C:\Program files"
            file_name="kernel32.dll"
    />
    <file
            source_path="/var/log"
            destination_path="/etc"
            file_name="server.log"
    />
</config>


Задача 2
Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите программу, читающую данный файл и проверяющую целостность файлов.
Пример
Файл сумм:
file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906
file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709
Пример вызова:  
<your program> <path to the input file> <path to the directory containing the files to check>
Формат вывода:
file_01.bin OK
file_02.bin FAIL
file_03.bin NOT FOUND
file_04.txt OK


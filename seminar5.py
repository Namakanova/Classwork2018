#Метод сплит. Есть строка и в ней элементы, разделенные символом.

cities = "Ufa Moscow Rio"
cities_list = cities.split() #если разделитель пробел
print(cities_list)           # еси другой: split(',') - в случае с запятой. Разделитель может состоять из любого числа символов
for city in cities_list:     #пробельные символы- пробелы, сиволы табуляции и все, что разделяет текст
    print (city)
cofee = 'arabic robust  liberyc'
print(cofee.split())   #любой набор пробельных символов. даже если несколько пробелов
print(cofee.split(' '))

#с другими сиволами пропустить подряд несколько одинаковых и считать их за один - нельзя (на уровне сплита, регулярки помогут)

#оператор in (без фор): является строка а подстрокой строки в?

s = 'abcd'
if 'z' in s: #or 'if z not in s' 
    print ('z - part of', s)

#чтение файла. utf-8 - универс. кодировка, умеет поддерживать много разных символов


# DANGER! ТАК ДЕЛАТЬ НЕ НАДО, ЭТО АНТИПРИМЕР (но в функциях так можно)

fh = open ('ref.txt', encoding='utf-8') #open просто открывает, но не читает encoding - именованный аргумент, рядом с ними нет пробела
text = fh.read() #прочли файл, запомнили инфу в переменную, можем закрыть файл
fh.close()  #обязательно закрыть файл, чтобы другие программы могли его изменять. 
print(text)

# Лучше делать так

with open('ref.txt'. encoding='utf-8') as fh: #внутри этого блока все операции с открытым файлом
    text = fh.read()
    print(fh.closed) #можем спросить, закрыт ли файл (здесь еще открыт)
print(fh.closed)# (здесь уже закрыт) при выходе из блока with open файл автоматически закрывается


#необязательно читать файл целиком. можно строчка за строчкой, постепенно
with open('ref.txt'. encoding='utf-8') as fh:
    lines = fh.readlines() #список из строк(str), состоящий из строчек (после каждой строчки есть невидимый символ)
for line i lines:
    print('+++++')
    print(line)

with open('ref.txt'. encoding='utf-8') as fh:
    for line in fh: #при итерации файла получаем строчки, из которых он состоит
        print('+++') #не переносим сразу весь файл, а по строчке заносим информацию
        print(line)

#как убрать знаки препинания
 s = 'Муха, уходи.'
 s_wo_dots = s.replace ('.', '')      #wo = WithOut, заменить ('что', 'на что')
 s_wo_commas = s_wo_dots.replace(',', '')
 s = s. replace('.', '').replace(',',  '') # с пом. методов не меняем переменную, а присваиваем новые данные
 words = s.split() #сплит всегда делает список из строк
print(words)

with open('ref.txt'. encoding='utf-8') as fh:
    text = fh.read()
text = text.replace (',', ''),replace('.',  '')
words = text. split()
print(len(words)) #колво слов в файле


#Число слов в строке
with open('ref.txt'. encoding='utf-8') as fh:
    for line in fh:
        line = text.replace (',', ''),replace('.',  '') #необязательно, ведь не влияет на число слов. Но важно если нужно число букв в словах
        line_words = line.split()
        print(len(line_words))

#каждый из вышеопис. способов оставляет символ переноса строки. А что если не хотим его считать?
with open('ref.txt'. encoding='utf-8') as fh:
    text = fh.read()
    lines = text.splitlines() #получим отдельыне строки без знака переноса
    #lines = fh.read().splitlines()
        
        

        





    






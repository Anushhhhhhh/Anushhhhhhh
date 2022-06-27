##4 Корочка Python: 
#структуры кода
#Продлеваем строки с помощью символа \
# Day 2. 22/06/2022

alphabet = " "
alphabet += "abcdefgh"
alphabet += "ijklmn"
alphabet
## Or I can do in another way
alphabet = "abcdefgh" +  "ijklmn"

## Сравниваем выражения 
## с помощью операторов if, elif и else

disaster = False

##
if disaster:
    print("Yes")
else:
    print("No")
### If else , else
furry = False
small = False
if furry:
    if small:
        print("It's a cat")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a shrink")
    else:
        print("It's a human. Or a hairless bear.")
## if, elif
color = "yellow"
if color =="red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what's that!")
else:
    print("No color available",color)
### Operators
x=7
x==7
x==1000
5<x
x<10
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###
####
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
5<x and 8==x
5<x or 8==x
5<x and not 5==x
##Если вы используете оператор and для того, чтобы объединить несколько проверок, Python позволит вам сделать следующее:
5 < x < 10 > 999
###
some_list = ["Hey"]
if some_list:
    print("Some_List")
else:
    print("Hello World")
## Повторяем действия с помощью while
count = 3
while count <= 10:
    print(count)
    count += 3
## 
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
## Пропускаем итерации # с помощью continue
# p.107

## Day 3. 24.06.2022
print("Hello")
## 
## Пропускаем итерации с помощью continue
# Иногда вам нужно не прерывать весь цикл, а только пропустить по какой-то причине одну итерацию
#numb
while True:
    value = input("Integer, please [q to quit]: ")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)
## Проверяем, завершился ли цикл заранее, с помощью else
numbers = [1, 3, 5]
position = 5
while position < len(numbers):
    number = numbers[position]
    if number % 2 ==0:
        print("Found even number", number)
        break
    position += 1
else: # break not called
    print("No even number found")
## Выполняем итерации с помощью for
## Вполне возможно пройти по последовательности таким образом:
rabbits = ["Flopsy", "Mopsy", " Cottonnail", "Peter"]
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1
## Однако существует более характерный для Python способ решения этой задачи:
for rabbit in rabbits:
    print(rabbit)
###
word = "dog"
for letter in word:
    print(letter)
### Итерирование по словарю (или его функции keys()) возвращает ключи.
Audit = {"Audit": "Davlatyor", "Financier": "Hojimurod", "Director": "Bakhtiyor"}
for card in Audit:
    print(card)
##Чтобы итерировать по значениям, а не по ключам, следует использовать функцию values():
Audit = {"Audit": "Davlatyor", "Financier": "Hojimurod", "Director": "Bakhtiyor"}
for card in Audit.values():
    print(card)
## Чтобы вернуть как ключ, так и значение кортежа, вы можете использовать функцию items():
for item in Audit.items():
    print(item)
## 
for card, contents in Audit.items():
    print("Nomush", card, " korush", contents)
###
## Day 3. 25/06/2022
# Прерываем цикл с помощью break
for card, contents in Audit.items():
    print("Nomush", card, " korush", contents)
    break
## Добавление ключевого слова continue в цикл for позволяет перейти на следующую итерацию цикла, как и в случае с циклом while.
for card, contents in Audit.items():
    print("Nomush", card, " korush", contents)
    continue
print("Anush")
## Let's check whether cycle has been finished earlier by using function ELSE
cheeses = []
for cheese in cheeses:
    print("There are no any cheese called ", cheeses)
    break
else:
    print("I told you no cheese in here")
## How to use Zip and why is it needed?
days = ["Monday", "Tuesday", "Wednesday"]
fruits = ["banana", "strawberry", "peach"]
drinks = ["coffee", "tea", "martini"]
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, ": drink",drink, "eat",fruit)
## Tuples
english = "monday", "tuesday", "wednesday"
french = "Lundi", "Mardi", "Mercedi"
# Now let's use zip to combine both of them
list(zip(english,french))
## We can make a dictionary out of the tuples by using zip()
dict(zip(english,french))
##Генерирование числовых последовательностей с помощью функции range()
## Range
for y in range(10,0,-1):
    print(y)
## Alter it to list
list(range(10,1, -1))
##
##В следующем фрагменте кода используется шаг 2, чтобы получить все четные числа от 0 до 10:
list(range(0,30,2))
##В следующем фрагменте кода используется шаг 2, чтобы получить все четные числа от 0 до 10:
list(range(0,30,3))
##В следующем фрагменте кода используется шаг 2, чтобы получить все четные числа от 0 до 10:
list(range(0,30,5))
# How it works without a launcher
list_of_numbers = []
list_of_numbers.append(1)
list_of_numbers.append(2)
list_of_numbers.append(3)
list_of_numbers.append(4)
list_of_numbers.append(5)
list_of_numbers
## Or we can do it by using the launcher
list_of_numbers = []
for number in range(0,100,20):
    list_of_numbers.append(number)
list_of_numbers
## or we could alter its type to range
list_of_numbers =list(range(100,10,-10))
list_of_numbers
##Вот так выглядит включение списка целых чисел
num_list = [number for number in range(1,10)]
num_list
##Другой способ
num_list_oo = [number-1 for number in range(1,10)]
num_list_oo
# Also we can add conditionals in launchers
a_list = [number for number in range(1,10) if number % 3 == 0]
a_list
# Also we can add conditionals in launchers
a_list = [number for number in range(1,100,10) if number > 50]
a_list
##
## Using for several times in a code Наконец, точно так же, как и в случае вложенных циклов, можно написать более чем один набор операторов for
rows = range(1,50,10)
cols = range(50,1,-10)
for row in rows:
    for col in cols:
        print(row,col)
##
rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)
## Launching dictionaries
word = "letters"
letters_counts = {letter: word.count(letter) for letter in word}
letters_counts
## Launchers for mnojestva
a_set = {number for number in range(1,6) if number % 3 ==1}
a_set
## Включение генератора
number_generator = (number for number in range(1,6))
number_generator
print(number_generator)
type(number_generator)
## You can iterate as much as you can by using generators 
for number in number_generator:
    print(number)
###
number_generator = list(number_generator)
number_generator
##3 You can use generators more than once
try_again = list(number_generator)
try_again
## 4

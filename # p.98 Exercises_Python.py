# p.98 Exercises 
#1.
year_list = [1995, 1996, 1997, 1998, 1999, 2000]
#2.
# 1998 was my 3rd birthday
#3.
# Answer : 2 000
#4.
#Создайте список things, содержащий три элемента: "mozzarella", "cinderella", 
#"salmonella".
things = ["mozzarella", "salmonella", "cinderella"]
#
things[2].upper()
#
things
## 
#6. Переведите сырный элемент списка things в верхний регистр целиком и выведите список
things[[0, 1]].upper() --????
##
#7.Удалите болезнь из списка things, получите Нобелевскую премию и затем выведите список на экран.
del things[0]
#
things
#8.Create a list that is called surprise and contains values as "Groucho", "Chico", "Harpo"
surprise = ["Groucho", "Chico", "Harpo"]
surprise
## 9.9. Напишите последний элемент списка surprise 
#со строчной буквы, затем обратите его и напишите с прописной буквы.
surprise[2].upper()
surprise[2].lower()
##10.
# Creating a new dictionary e2f
e2f = {"dog":"chien", "cat":"chat", "walrus":"morse"}
e2f
##11.Используя словарь e2f, выведите
# французский вариант слова walrus.
e2f["walrus"]
#12. Создайте французско-английский словарь 
##f2e на основе словаря e2f. Используйте метод items.
ef2 = {"chien" :"dog", "chat":"cat", "morse": "walrus"}
ef2
#13. Get the english translation of Chien
ef2["chien"]
# 14. Создайте и выведите на экран множество английских
# слов из ключей словаря e2f -- ????
#15.15. Создайте многоуровневый словарь life. Используйте следующие строки для 
## ключей верхнего уровня: 'animals', 'plants' и 'other'. Сделайте так, чтобы ключ 
## 'animals' ссылался на другой словарь, имеющий ключи 'cats', 'octopi' и 'emus'. 
# Сделайте так, чтобы ключ 'cats' ссылался на список строк со значениями 'Henri', 
##'Grumpy' и 'Lucy'. Остальные ключи должны ссылаться на пустые словари
## ????? --- 15.
#


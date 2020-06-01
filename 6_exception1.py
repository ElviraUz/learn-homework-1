"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

dictionary = {
  "Как дела": "Хорошо!",
  "Что делаешь?": "Программирую",
  "Есть ли жизнь на Марсе?":"42",
  "Название нашей планеты":"Земля"
  }
  
def ask_user_dict(dictionary):
  try:
    while True:
      question = input("Пользователь: ")
      if question in  dictionary:
        print (f"Программа: {dictionary[question]}")
      elif question == "пока":
        print("До свидания!")
        break
      else:
          print ("Программа:Введите другой вопрос")

  except KeyboardInterrupt:
    print ("Пока!")
    break

if __name__ == "__main__":
    ask_user_dict(dictionary)
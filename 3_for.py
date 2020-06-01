"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [
    {'school_class': '4a', 'class_scores': [1,2,3,4,5]}, 
    {'school_class': '4b', 'class_scores': [5,3,1,5,32]},
    {'school_class': '4c', 'class_scores': [2,4,1,5,5]}
]

def main():
    scores_sum = 0
    for scores in school:
      avg_school_class = sum(scores['class_scores'])/len(scores['class_scores'])
      print (f'Средний балл по классу: {avg_school_class}')
      scores_sum = scores_sum+avg_school_class / len(school)
    print (f'Средний бал по школе: {scores_sum/len(school)}"')

if __name__ == "__main__":
    main()
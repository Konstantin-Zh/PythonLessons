# Начальные условия задачи
grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print (grades)
print (students)

# 1 шаг - Сортируем в алфавитном порядке имена учеников и приводим их в соответствие порядку оценок
students = sorted(list(students), key=str.upper)
print (students)

# 2 шаг - Вычисляем среднее арифметическое по оценка каждого ученика
av_grades = [(sum(grades[0])/len(grades[0])), (sum(grades[1])/len(grades[1])), (sum(grades[2])/len(grades[2])), (sum(grades[3])/len(grades[3])), (sum(grades[4])/len(grades[4]))]
print (av_grades)

# 3 щаг - Составляем словрь с именами учеников (ключ) и значениями их средних оценок (значение)
dict = {students[0]: av_grades[0], students[1]: av_grades[1], students[2]: av_grades[2], students[3]: av_grades[3], students[4]: av_grades[4]}
print (dict)
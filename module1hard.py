grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# 1. Переведём множество в список
students_1 = list(students)
print(students_1) #['Steve', 'Aaron', 'Bilbo', 'Johnny', 'Khendrik'] НЕ в алфавитном порядке

# 2. Упорядочим список по алфавиту
students_2 = sorted(students_1)
print(students_2) #['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve'] в алфавитном порядке

# 3. Находим средний балл
grades_A = grades[0]
print(grades_A) # [5, 3, 3, 5, 4]
average_A = (sum(grades_A) / len(grades_A))
print(average_A) # 4.0

grades_B = grades[1]
print(grades_B) # [2, 2, 2, 3]
average_B = (sum(grades_B) / len(grades_B))
print(average_B) # 2.25

grades_J = grades[2]
print(grades_J) # [4, 5, 5, 2]
average_J= (sum(grades_J) / len(grades_J))
print(average_J) # 4.0

grades_K = grades[3]
print(grades_K) # [4, 4, 3]
average_K = (sum(grades_K) / len(grades_K))
print(average_K) # 3.6666666666666665

grades_S= grades[4]
print(grades_S) # [5, 5, 5, 4, 5]
average_S = (sum(grades_S) / len(grades_S))
print(average_S) # 4.8

# 4. Составляем новый список из полученных средних
grades_average = [average_A, average_B, average_J, average_K, average_S]
print(grades_average) # [4.0, 2.25, 4.0, 3.6666666666666665, 4.8]

# 5. Составляем словарь
students_average_dictionary = dict(zip(students_2,grades_average ))
print(students_average_dictionary) # {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

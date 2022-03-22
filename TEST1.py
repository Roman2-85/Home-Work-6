class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        self.grades = {}
        self.av_score = []
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        av_s = ''.join(map(str, self.av_score))
        c_in_prog = ', '.join(map(str, self.courses_in_progress))
        f_c = ', '.join(map(str, self.finished_courses))
        text = f'Имя студента: {self.name} \nФамилия студента: {self.surname} \nСредняя оценка за домашнее задание: {av_s} \nКурсы в процессе изучения: {c_in_prog} \nЗавершенные курсы: {f_c}' 
        
        return text


    def cal_av_score(self):
        all_grades = []
        for score in self.grades.values():
            all_grades += score
        self.av_score.append(round(sum(all_grades) / len(all_grades), 2))
       
        return self.av_score 
    
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.av_score < other.av_score
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.av_score = []
        
    def __str__(self):
        av_s = ''.join(map(str, self.av_score)) 
        text = f'Имя лектора: {self.name} \nФамилия лектора: {self.surname} \nСредняя оценка за лекции: {av_s}' 
        
        return text

    def cal_av_score(self):
        all_grades = []
        for score in self.grades.values():
            all_grades += score
        self.av_score.append(round(sum(all_grades) / len(all_grades), 2))
       
        return self.av_score 

           
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.av_score < other.av_score
    
class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
   
    def __str__(self):
        text = f'Имя эксперта: {self.name} \nФамилия эксперта: {self.surname}' 
        
        return text

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']

student2 = Student('Ray', 'Charles', 'your_gender')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']

lecturer1 = Lecturer('Roy', 'John')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Galla', 'Roll')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('John', 'Travolta')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Bryan', 'May')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student1, 'Git', 10)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 4)
reviewer2.rate_hw(student2, 'Git', 9.5)
reviewer2.rate_hw(student2, 'Git', 9)

Student.rate_hw(student1, lecturer1, 'Python', 8)
Student.rate_hw(student1, lecturer1, 'Python', 9)
Student.rate_hw(student1, lecturer1, 'Git', 9)
Student.rate_hw(student1, lecturer1, 'Git', 8)

Student.rate_hw(student2, lecturer2, 'Python', 7)
Student.rate_hw(student2, lecturer2, 'Python', 8)
Student.rate_hw(student2, lecturer2, 'Git', 8.5)
Student.rate_hw(student2, lecturer2, 'Git', 9)


# Оценки студентов 
print(student1.grades)
print(student2.grades)
print('==================================')

# Оценки лекторов

print(lecturer1.grades)
print(lecturer2.grades)
print('==================================')

# Средняя оценка за домашние задания первого студента 
student1.cal_av_score()
print(student1)
print('==================================')

# Средняя оценка за домашние задания второго студента 
student2.cal_av_score()
print(student2)
print('==================================')

# Средняя оценка за лекции первого лектора
lecturer1.cal_av_score()
print(lecturer1)

print('==================================')
# Средняя оценка за лекции второго лектора
lecturer2.cal_av_score()
print(lecturer2)
print('==================================')

print(reviewer1)
print('==================================')
print(reviewer2)
print('==================================')


student_list = [student1, student2]

def avg_student_grade(s_list, course):
    s = []
    for i in s_list:
        if course in i.grades:
            s.append(i.grades[course])
    all_grades = []
    for j in s:
        all_grades += j     
    avg = round(sum(all_grades) / len(all_grades), 2)
    print(f'{avg} - cредняя оценка за домашние задания по всем студентам в рамках курса {course}') 
     

avg_student_grade(student_list, 'Git')

lecturer_list = [lecturer1, lecturer2]

def avg_lecturer_grade(l_list, course):
    s = []
    for i in l_list:
        if course in i.grades:
            s.append(i.grades[course])   
    all_grades = []
    for j in s:
        all_grades += j     
    avg = round(sum(all_grades) / len(all_grades), 2)
    print(f'{avg} - cредняя оценка за лекции всех лекторов в рамках курса {course}')
    

avg_lecturer_grade(lecturer_list, 'Git')


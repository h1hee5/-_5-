class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = english_score + c_score + python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()
    
    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif self.average_score >= 80:
            return 'B'
        elif self.average_score >= 70:
            return 'C'
        elif self.average_score >= 60:
            return 'D'
        else:
            return 'F'

def input_student_info():
    students = []
    for _ in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        c_score = int(input("C 언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))
        student = Student(student_id, name,  english_score,  c_score,  python_score)
        students.append(student)
    return students

def calculate_total_average(students):
    total_sum = sum(student.total_score for student in students)
    average = total_sum / len(students)
    return total_sum, average

def calculate_rank(students):
    students.sort(key=lambda x: x.total_score, reverse=True)
    for i, student in enumerate(students):
        student.rank = i + 1

def count_students_above_80(students):
    count = sum(1 for student in students if student.total_score >= 240)  # 80 * 3
    return count

def print_student_info(students):
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "학번", "이름", "영어", "C언어", "파이썬", "총점", "평균", "학점"))
    for student in students:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            student.student_id, student.name, student.english_score, student.c_score, student.python_score,
            student.total_score, round(student.average_score, 2), student.grade))
    print()

def main():
    students = input_student_info()
    total_sum, average = calculate_total_average(students)
    calculate_rank(students)
    above_80_count = count_students_above_80(students)
    
    print_student_info(students)
    print("전체 학생 수: ", len(students))
    print("총점 평균: ", total_sum)
    print("전체 평균: ", round(average, 2))  # 평균값을 소수점 두 자리수까지 반올림
    print("80점 이상 학생 수: ", above_80_count)

if __name__ == "__main__":
    main()

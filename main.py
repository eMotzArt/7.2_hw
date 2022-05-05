import json
from functions import json_file_to_mem, get_student_by_pk, student_info, get_profession_by_title, check_fitness

def main():
    # получаем номер студента для поиска
    pk = int(input("Введите номер студента: "))

    # считываем всех студентов
    students = json_file_to_mem('students.json')

    # ищем студента по номеру
    student = get_student_by_pk(students, pk)
    # если студент найден
    if student:
        print(*(student_info(student)), sep='\n')
    # если не найден
    else:
        print("У нас нет такого студента")
        return

    # получаем название профессии для сравнения
    prof = input(f"Выберите специальность для оценки студента {student['full_name']}: ")

    # считываем все профессии
    professions = json_file_to_mem('professions.json')

    #ищем профессию по навзанию
    profession = get_profession_by_title(professions, prof)

    # если профессия найдена
    if profession:
        result = check_fitness(student, profession)
        print(f"Пригодность {result['fit_percent']}%",
              f"{student['full_name']} знает {', '.join(result['has'])}" if len(result['has']) > 0 else "",
              f"{student['full_name']} не знает {', '.join(result['lacks'])} " if len(result['lacks'])>0 else "",
              sep='\n'
              )
    #если не найдена
    else:
        print("У нас нет такой специальности")
        return

if __name__ == "__main__":
    main()
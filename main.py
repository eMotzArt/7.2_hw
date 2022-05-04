import json

def json_file_to_mem(file_name):
    with open(file_name) as file:
        content = json.load(file)
    return content

def get_student_by_pk(list_, pk):
    for item in list_:
        if item['pk'] == pk:
            return item
    return False

def student_info(student):
    name_info = f"Студент {student['full_name']}"
    skills_info = f"Знает: {(', '.join(student['skills'])).rstrip()}"
    learns_info = f"Хочет изучить: {(', '.join(student['learns'])).rstrip()}"

    return name_info, skills_info, learns_info

def get_profession_by_title(list_, title):
    for item in list_:
        if item['title'] == title:
            return item
    return False

def check_fitness(student, profession):
    student_skills = set(student['skills'])
    prof_skills = set(profession['skills'])
    check_result = {
        "has": list(student_skills.intersection(prof_skills)),
        "lacks": list(prof_skills.difference(student_skills)),
        "fit_percent": round(100 / len(prof_skills) * len(student_skills.intersection(prof_skills)))
    }

    return check_result


def main():
    pk = int(input("Введите номер студента: "))

    students = json_file_to_mem('students.json')
    professions = json_file_to_mem('professions.json')

    student = get_student_by_pk(students, pk)
    if student:
        print(*(student_info(student)), sep='\n')
    else:
        print("У нас нет такого студента")
        return

    prof = input(f"Выберите специальность для оценки студента {student['full_name']}: ")
    profession = get_profession_by_title(professions, prof)
    if profession:
        result = check_fitness(student, profession)
        print(f"Пригодность {result['fit_percent']}%",
              f"{student['full_name']} знает {', '.join(result['has'])}" if len(result['has']) > 0 else "",
              f"{student['full_name']} не знает {', '.join(result['lacks'])} " if len(result['lacks'])>0 else "",
              sep='\n'
              )
    else:
        print("У нас нет такой специальности")
        return

if __name__ == "__main__":
    main()
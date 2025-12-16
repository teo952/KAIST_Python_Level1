def new_student(student_info):
    student_data = {}
    
    if len(student_info) != 5:
        print("ERROR: student_info의 요소 수가 5가 아닙니다.")
        return {}
    
    # 이름
    name = student_info[0]
    if type(name) != str:
        print("ERROR: 이름이 문자열이 아닙니다.")
        return {}
    student_data['이름'] = name
    
    # 학교
    school = student_info[1]
    if type(school) != str or not school.endswith('학교'):
        print("ERROR: 학교 이름이 유효하지 않습니다.")
        return {}
    student_data['학교'] = school
    
    # 학년
    grade = student_info[2]
    if type(grade) != int or not (1 <= grade <= 6):
        print("ERROR: 학년이 1~6 사이의 정수가 아닙니다.")
        return {}
    student_data['학년'] = grade
    
    # 연락처
    tele = student_info[3]
    if type(tele) != str or len(tele) != 11 or not tele.isdigit():
        print("ERROR: 연락처가 올바르지 않습니다.")
        return {}
    student_data['연락처'] = tele
    
    # 수업
    course = student_info[4]
    course_list = ['Python', 'Java', 'C', 'C++']
    if type(course) != list or not all(c in course_list for c in course):
        print("ERROR: 수업 목록이 올바르지 않습니다.")
        return {}
    student_data['수업'] = course
    
    print(f"새로운 학생의 정보를 완성했습니다:\n{student_data}")
    return student_data

def get_student(student_list, key_value_list):
    candidate = []
    for student in student_list:
        match = True
        for key, value in key_value_list:
            if student.get(key) != value:
                match = False
                break
        if match:
            candidate.append(student)
    print(candidate)
    return candidate

def edit_student(student_db, key_value_list, edit_list):
    candidate_students = get_student(student_db, key_value_list)
    print("CANDIDATE STUDENTS:", candidate_students)
    
    for student in candidate_students:
        for key, value in edit_list:
            student[key] = value
    
    print("EDITED STUDENTS:", candidate_students)

student_infos = [
    ['한넙죽', '한국중학교', 1, '01012342345', ['Python', 'C']],
    ['김거위', '오근소등학교', 5, '01023334444', ['Python']],
    ['로라', '한국중학교', 2, '01032324242', ['C++', 'Java']],
    ['리사', '한국초등학교', 6, '01022223333', ['C', 'C++']],
    ['이철수', '대한초등학교', 5, '01022488888', ['C', 'Python']],
    ['남영희', '대한중학교', 1, '01022323333', ['Python', 'Java']]
]

student_infos_error = [
    ['한넙죽', '한국중학교', -1, '01012342345', ['Python', 'C']],
    ['김거위', '오리초', 5, '01023334444', ['Python']],
    ['로라', '한국중학교', 2, '1032324242', ['C++', 'Java']],
    ['리사', '한국초등학교', 6, '01022223333', ['C', 'C++', 'English']],
    ['이철수', '대한초등학교', '5', '01022488888', ['C', 'Python']],
    ['남영희', 1, '대한중학교', '01022323333', ['Python', 'Java']]
]

# 올바른 정보 테스트
for student_info in student_infos:
    new_st = new_student(student_info)

# 잘못된 정보 테스트
for student_info_error in student_infos_error:
    new_student(student_info_error)

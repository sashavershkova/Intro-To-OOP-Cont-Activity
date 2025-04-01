from school_schedule.student import Student

def test_student_instantiation():
    name = "Jenny"
    grade = "freshman"
    classes = ["Math", "Political science"]

    student = Student(name, grade, classes)

    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes
    assert len(student.classes) == 2

def test_student_instantiation_empty_classes():
    name = "Jenny"
    grade = "freshman"
    classes = []

    student = Student(name, grade, classes)

    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes
    assert len(student.classes) == 0

def test_add_class():

    name = "Jenny"
    grade = "freshman"
    classes = ["Math"]

    student = Student(name, grade, classes)

    student.add_class("Music")

    assert len(student.classes) == 2
    assert "Music" in classes
    assert student.add_class("Music") == student.classes

def test_get_num_classes():
    name = "Jenny"
    grade = "freshman"
    classes = ["Math", "Geography", "Music", "Art"]

    student = Student(name, grade, classes)
    result = student.get_num_classes()

    assert len(classes) == 4
    assert result == 4

def test_display_classes():
    name = "Jenny"
    grade = "freshman"
    classes = ["Math", "Geography", "Music", "Art"]

    student = Student(name, grade, classes)
    result = student.display_classes()

    assert result == "Math, Geography, Music, Art"

def test_summary():
    name = "Jenny"
    grade = "freshman"
    classes = ["Math", "Geography", "Music", "Art"]

    student = Student(name, grade, classes)
    result = student.summary()    

    assert result == "Jenny is a freshman enrolled in 4 classes: Math, Geography, Music, Art"
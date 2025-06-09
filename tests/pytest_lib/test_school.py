import pytest
from source.school import Classroom, Teacher, Student, TooMayStudents

@pytest.fixture
def hogwarts_classroom():
    """Creates a Hogwarts classroom with a teacher and some students."""
    professor_snape = Teacher("Severus Snape")
    students = [Student(name) for name in ["Harry Potter", "Hermione Granger", "Ron Weasley"]]
    return Classroom(professor_snape, students, "Potions")

@pytest.mark.parametrize("student_name", [
    "Draco Malfoy", "Luna Lovegood", "Neville Longbottom"
])
def test_add_student(hogwarts_classroom, student_name):
    """Test adding students to the Hogwarts classroom."""
    new_student = Student(student_name)
    hogwarts_classroom.add_student(new_student)
    assert new_student in hogwarts_classroom.students

def test_add_student_limit(hogwarts_classroom):
    """Test that adding too many students raises an exception."""
    for name in ["Draco Malfoy", "Luna Lovegood", "Neville Longbottom", "Cho Chang", "Cedric Diggory", "Fred Weasley", "George Weasley", "Ginny Weasley"]:
        hogwarts_classroom.add_student(Student(name))
    with pytest.raises(TooMayStudents):
        hogwarts_classroom.add_student(Student("Percy Weasley"))

@pytest.mark.parametrize("student_to_remove", [
    "Harry Potter", "Hermione Granger", "Ron Weasley"
])
def test_remove_student(hogwarts_classroom, student_to_remove):
    """Test removing students from the Hogwarts classroom."""
    hogwarts_classroom.remove_student(student_to_remove)
    assert all(student.name != student_to_remove for student in hogwarts_classroom.students)

@pytest.mark.parametrize("new_teacher_name", [
    "Albus Dumbledore", "Minerva McGonagall"
])
def test_change_teacher(hogwarts_classroom, new_teacher_name):
    """Test changing the teacher in the Hogwarts classroom."""
    new_teacher = Teacher(new_teacher_name)
    hogwarts_classroom.change_teacher(new_teacher)
    assert hogwarts_classroom.teacher.name == new_teacher_name

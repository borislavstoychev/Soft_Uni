from project.student import Student
import unittest


class StudentTest(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student("Bobby", {"mat": ["good job"]})

    def test_constructor(self):
        self.assertEqual("Bobby", self.student.name)
        self.assertEqual({"mat": ["good job"]}, self.student.courses)

    def test_enroll_course_in_courses(self):
        result = self.student.enroll("mat","good job", "be better")
        expect = "Course already added. Notes have been updated."
        self.assertEqual(expect, result)

    def test_enroll_course_in_courses_if_add_courses_is_empty_str(self):
        self.student = Student("Goshko", courses=None)
        result = self.student.enroll("bg", "good job", "")
        expect = "Course and course notes have been added."
        self.assertEqual(expect, result)
        self.assertEqual({"bg": "good job"}, self.student.courses)

    def test_enroll_course_in_courses_if_add_courses_is_Y(self):
        result = self.student.enroll("bg", "good job", "Y")
        expect = "Course and course notes have been added."
        self.assertEqual(expect, result)
        self.assertEqual({"mat": ["good job"], "bg": "good job"}, self.student.courses)

    def test_enroll_course_not_in_courses(self):
        result = self.student.enroll("bg", "good job", "bravo")
        expect = "Course has been added."
        self.assertEqual(expect, result)
        self.assertEqual({"mat": ["good job"], "bg": []}, self.student.courses)

    def test_add_notes_if_course_in_courses(self):
        result = self.student.add_notes("mat", "the best")
        expect = "Notes have been updated"
        self.assertEqual(expect, result)
        self.assertEqual({"mat": ["good job", "the best"]}, self.student.courses)

    def test_add_notes_if_course_not_in_courses(self):
        with self.assertRaises(Exception):
            self.student.add_notes("bg", "grumni se")

    def test_leave_course_if_in_courses(self):
        result = self.student.leave_course("mat")
        expect = "Course has been removed"
        self.assertEqual(expect, result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_if_not_in_courses(self):
        with self.assertRaises(Exception):
            self.student.leave_course("bg")



if __name__ == "__main__":
    unittest.main()
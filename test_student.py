import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_valid_marks(self):
        s = Student(1, "Rahul", 80)
        self.assertEqual(s.marks, 80)

    def test_invalid_marks(self):
        s = Student(1, "Rahul", 80)
        s.marks = 150   # invalid
        self.assertNotEqual(s.marks, 150)

    def test_update_marks(self):
        s = Student(1, "Rahul", 80)
        s.marks = 90
        self.assertEqual(s.marks, 90)


if __name__ == "__main__":
    unittest.main()
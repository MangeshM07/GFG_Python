import unittest
from unittest.mock import patch
from UnitTesting.employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class executes at the beginning")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tear down class executes at the end of program execution")

    def setUp(self):
        print("setup")
        self.emp1 = Employee('Corey', 'Schafer', 50000)
        self.emp2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print("Teardown")

    def test_email(self):
        print("Test email")
        self.assertEqual(self.emp1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp2.email, "Sue.Smith@email.com")

        self.emp1.first = 'John'
        self.emp2.first = "Jane"

        self.assertEqual(self.emp1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("Test fullname")
        self.assertEqual(self.emp1.fullname, "Corey Schafer")
        self.assertEqual(self.emp2.fullname, "Sue Smith")

        self.emp1.first = 'John'
        self.emp2.first = "Jane"

        self.assertEqual(self.emp1.fullname, "John Schafer")
        self.assertEqual(self.emp2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("Pay raise")
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad response!')


if __name__ == "__main__":
    unittest.main()

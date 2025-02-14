import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee1 = Employee("John", "Lennon", 1000)
        self.employee2 = Employee("Paul", "McCartney", -1500)
        self.employee3 = Employee("Ringo", "Starr", 0)
        self.employee4 = Employee("George", "Harrison", None)
        self.employees = [self.employee1, self.employee2, self.employee3, self.employee4]

    def test_email(self):
        for employee in self.employees:
            self.assertEqual(employee.email, f"{employee.first}.{employee.last}@email.com")

    def test_fullname(self):
        for employee in self.employees:
            self.assertEqual(employee.fullname, f"{employee.first} {employee.last}")

    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.pay, 1050)
        self.employee2.apply_raise()
        self.assertEqual(self.employee2.pay, -1575)
        self.employee3.apply_raise()
        self.assertEqual(self.employee3.pay, 0)
        with self.assertRaises(TypeError):
            self.employee4.apply_raise()
        self.assertEqual(self.employee4.pay, None)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get_response):
        mock_get_response.return_value.ok = True
        self.assertEqual(self.employee1.monthly_schedule("March"), mock_get_response().text)
        self.assertEqual(self.employee2.monthly_schedule("June"), mock_get_response().text)
        mock_get_response.return_value.ok = False
        self.assertEqual(self.employee3.monthly_schedule("July"), "Bad Response!")
        self.assertEqual(self.employee4.monthly_schedule("January"), "Bad Response!")


if __name__ == "__main__":
    unittest.main()

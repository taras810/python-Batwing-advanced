import unittest
from unittest.mock import patch
from employee import Employee


class TestForEmployee(unittest.TestCase):
    def setUp(self):
        self.TestEmployee = Employee("Taras", "Senko", 1000)

    def test_email(self):
        self.assertEqual(self.TestEmployee.email, "Taras.Senko@email.com")

    def test_fullname(self):
        self.assertEqual(self.TestEmployee.fullname, "Taras Senko")

    def test_apply_raise(self):
        self.TestEmployee.apply_raise()
        self.assertEqual(self.TestEmployee.pay, 1050)

    @patch('employee.requests')
    def test_monthly_schedule(self, mock_requests):
        mock_requests.get().ok = True
        mock_requests.get().text = "Sample text"
        self.assertEqual(self.TestEmployee.monthly_schedule("12"), "Sample text")

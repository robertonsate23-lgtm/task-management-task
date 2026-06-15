# test_validation.py
import unittest
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

class TestValidation(unittest.TestCase):

    def test_validate_task_title_valid(self):
        """Should return True for a normal, valid title."""
        self.assertTrue(validate_task_title("Finish Lab Assignment"))

    def test_validate_task_title_empty(self):
        """Should return False for empty strings or pure whitespace."""
        self.assertFalse(validate_task_title(""))
        self.assertFalse(validate_task_title("   "))

    def test_validate_task_title_too_long(self):
        """Should return False if the title exceeds 50 characters."""
        long_title = "A" * 51
        self.assertFalse(validate_task_title(long_title))

    def test_validate_task_description_valid(self):
        """Should return True for a standard description."""
        self.assertTrue(validate_task_description("Write unit tests for the package modules."))

    def test_validate_task_description_empty(self):
        """Should return False for blank descriptions."""
        self.assertFalse(validate_task_description(""))

    def test_validate_due_date_correct_format(self):
        """Should return True for valid YYYY-MM-DD dates."""
        self.assertTrue(validate_due_date("2026-06-15"))

    def test_validate_due_date_wrong_format(self):
        """Should return False for mismatched structures like DD-MM-YYYY."""
        self.assertFalse(validate_due_date("15-06-2026"))

    def test_validate_due_date_invalid_calendar_day(self):
        """Should return False for dates that don't exist on the calendar."""
        self.assertFalse(validate_due_date("2026-02-30"))  # February 30th

if __name__ == "__main__":
    unittest.main()
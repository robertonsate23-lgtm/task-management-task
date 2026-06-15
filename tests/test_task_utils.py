# test_task_utils.py
import unittest
from task_manager.task_utils import tasks, add_task, mark_task_as_complete, calculate_progress

class TestTaskUtils(unittest.TestCase):

    def setUp(self):
        """Resets the shared global tasks list before every single test run."""
        tasks.clear()

    def test_add_task_success(self):
        """Verifies a valid task appends cleanly into the data array with standard keys."""
        result = add_task("Read Book", "Finish reading mystery novel", "2026-07-01")
        self.assertTrue(result)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Read Book")
        self.assertFalse(tasks[0]["completed"])  # Verifies it defaults to False

    def test_add_task_validation_failure(self):
        """Verifies a task with bad data fails addition constraints and isn't saved."""
        result = add_task("", "Description with missing title", "2026-07-01")
        self.assertFalse(result)
        self.assertEqual(len(tasks), 0)

    def test_mark_task_as_complete_success(self):
        """Verifies 1-indexed items map to arrays and flip flags correctly."""
        add_task("Fix Bug", "Resolve routing issue", "2026-06-20")
        result = mark_task_as_complete("1")  # User passes string "1" for first item
        self.assertTrue(result)
        self.assertTrue(tasks[0]["completed"])

    def test_mark_task_as_complete_out_of_bounds(self):
        """Verifies an invalid array position string gracefully stops crashes."""
        add_task("Fix Bug", "Resolve routing issue", "2026-06-20")
        result = mark_task_as_complete("99")  # Non-existent index
        self.assertFalse(result)

    def test_mark_task_as_complete_invalid_input(self):
        """Verifies non-numeric inputs don't crash the script run."""
        add_task("Fix Bug", "Resolve routing issue", "2026-06-20")
        result = mark_task_as_complete("abc")  # Bad typing string
        self.assertFalse(result)

    def test_calculate_progress_empty(self):
        """Verifies 0.0 metrics output safely when zero assignments are on record."""
        self.assertEqual(calculate_progress(), 0.0)

    def test_calculate_progress_accurate_ratio(self):
        """Verifies system computes math divisions cleanly across completed fractions."""
        add_task("Task 1", "Desc 1", "2026-06-25")
        add_task("Task 2", "Desc 2", "2026-06-25")
        
        mark_task_as_complete("1")  # 1 out of 2 tasks complete = 50%
        self.assertEqual(calculate_progress(), 50.0)

if __name__ == "__main__":
    unittest.main()
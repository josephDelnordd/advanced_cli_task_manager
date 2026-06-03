import unittest
import os
from task_manager.core import add_task, load_tasks, delete_task

TEST_FILE = "test_tasks.json"

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        os.environ["TASKS_FILE_PATH"] = TEST_FILE
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_add_task(self):
        task = add_task("Test task", "high")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(task["description"], "Test task")

    def test_delete_task(self):
        task = add_task("To delete", "low")
        delete_task(task["id"])
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
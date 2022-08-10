import unittest
from scr.hello_world_folder import run_hello_world


class TestHelloWorldTestCase(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(run_hello_world(), "hello world")

import unittest
from src.sample.Note import Note


class TestNote(unittest.TestCase):
    def setUp(self) -> None:
        self.note = Note("kolokwium", 4)

    def test_get_name(self):
        self.assertEqual(self.note.get_name, "kolokwium")

    def tearDown(self) -> None:
        self.note = Note

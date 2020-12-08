import unittest
from src.sample.Note import Note


class TestNote(unittest.TestCase):
    def setUp(self) -> None:
        self.note = Note("kolokwium", 4)

    def test_get_name(self):
        self.assertEqual(self.note.get_name, "kolokwium")

    def test_get_note(self):
        self.assertEqual(self.note.get_note, 4)

    def tearDown(self) -> None:
        self.note = Note

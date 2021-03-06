import unittest
from src.sample.Note import Note


class TestNote(unittest.TestCase):
    def setUp(self) -> None:
        self.note = Note("kolokwium", 4)

    def test_get_name(self):
        self.assertEqual(self.note.get_name, "kolokwium")

    def test_get_note(self):
        self.assertEqual(self.note.get_note, 4)

    def test_name_is_None_raises_exception(self):
        self.assertRaises(ValueError, Note, None, 4)

    def test_name_is_empty_raises_exception(self):
        self.assertRaises(ValueError, Note, "", 4)

    def test_note_out_of_range_1(self):
        self.assertRaises(ValueError, Note, "kolokwium", 1)

    def test_note_out_of_range_7(self):
        self.assertRaises(ValueError, Note, "kolokwium", 7)

    def test_note_in_range_float_4_point_5(self):
        note = Note("kolokwium", 4.5)
        self.assertEqual(note.get_note, 4.5)

    def test_note_in_range_float_4_point_2_raises_exception(self):
        self.assertRaises(ValueError, Note, "kolokwium", 4.2)

    def tearDown(self) -> None:
        self.note = Note

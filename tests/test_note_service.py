from unittest.mock import *
import unittest
from src.sample.NotesStorage import *
from src.sample.NotesService import *
from src.sample.Note import Note


class TestNote(unittest.TestCase):
    def setUp(self):
        self.note_service = NotesService()

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_add_note(self, mock_method):
        mock_method.return_value = [Note("chemistry", 5)]
        self.note_service.add(Note("chemistry", 5))
        self.assertEqual(self.note_service.notes_storage.getAllNotesOf("chemistry")[0].note, 5)

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_average(self, mock_method):
        mock_method.return_value = [Note("chemistry", 5), Note("chemistry", 4)]
        self.assertEqual(self.note_service.averageOf("chemistry"), 4.5)

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_average_no_notes_exception(self, mock_method):
        mock_method.return_value = []
        self.assertRaises(ZeroDivisionError, self.note_service.averageOf, "chemistry")

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_average_name_incorrect(self, mock_method):
        mock_method.return_value = [Note("biology", 5), Note("biology", 4)]
        self.assertRaises(ValueError, self.note_service.averageOf, "chemistry")

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_clear(self, mock_method):
        mock_method.return_value = [Note("chemistry", 5), Note("chemistry", 4)]
        self.note_service.clear()
        mock_method.return_value = []
        self.assertEqual(self.note_service.notes_storage.getAllNotesOf("chemistry"), [])
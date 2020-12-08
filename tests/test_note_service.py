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
        result = self.note_service.add(Note("chemistry", 5))
        self.assertEqual(self.note_service.averageOf("chemistry"), 5)
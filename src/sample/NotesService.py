from src.sample.NotesStorage import NotesStorage


class NotesService:
    def __init__(self):
        self.notes_storage = NotesStorage()

    def add(self, note):
        self.notes_storage.add(note)

    def averageOf(self, name):
        all_notes = self.notes_storage.getAllNotesOf(name)
        if len(all_notes) != 0:
            if name != all_notes[0].name:
                raise ValueError("Incorrect name!")
            else:
                suma = 0
                for note in all_notes:
                    suma += note.note
                return suma/len(all_notes)
        else:
            raise ValueError("Empty list!")

    def clear(self):
        self.notes_storage.clear()

class Note:
    def __init__(self, name, note):
        if name is None:
            raise ValueError("Name cannot be none")
        elif name == "":
            raise ValueError("Name cannot be empty")
        else:
            self.name = name
        if note in [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]:
            self.note = note
        else:
            raise ValueError("Note not in range")

    @property
    def get_name(self):
        return self.name

    @property
    def get_note(self):
        return self.note


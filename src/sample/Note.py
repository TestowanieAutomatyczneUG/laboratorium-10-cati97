class Note:
    def __init__(self, name, note):
        if name is None:
            raise ValueError("Name cannot be none")
        elif name == "":
            raise ValueError("Name cannot be empty")
        else:
            self.name = name
        if 2 <= note <= 6:
            self.note = note
        else:
            raise ValueError("Note not in range")

    @property
    def get_name(self):
        return self.name

    @property
    def get_note(self):
        return self.note


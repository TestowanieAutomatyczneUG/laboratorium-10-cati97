class Note:
    def __int__(self, name, note):
        if name is not None or name != "":
            self.name = name
        else:
            raise ValueError("Name cannot be none")
        if 2 <= note <= 6:
            self.note = note
        else:
            raise ValueError("Note not in range")

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note

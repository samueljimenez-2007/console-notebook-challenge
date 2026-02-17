from datetime import datetime


class Note:

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code, title, text, importance):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags = []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return "Date: " + str(self.creation_date) + "\n" + self.title + ": " + self.text


class Notebook:

    def __init__(self):
        self.notes = []

    def add_note(self, title, text, importance):
        code = len(self.notes) + 1

        note = Note(code, title, text, importance)
        self.notes.append(note)

        return code

    def delete_note(self, code):
        for note in self.notes:
            if note.code == code:
                self.notes.remove(note)
                break

    def important_notes(self):
        important = []

        for note in self.notes:
            if note.importance == Note.HIGH or note.importance == Note.MEDIUM:
                important.append(note)

        return important

    def notes_by_tag(self, tag):
        result = []

        for note in self.notes:
            if tag in note.tags:
                result.append(note)

        return result

    def tag_with_most_notes(self):

        tag_count = {}

        for note in self.notes:
            for tag in note.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1

        if len(tag_count) == 0:
            return ""

        max_count = 0
        most_used_tag = ""

        for tag in tag_count:
            if tag_count[tag] > max_count:
                max_count = tag_count[tag]
                most_used_tag = tag

        return most_used_tag

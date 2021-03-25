import json


class Library:
    def __init__(self):
        try:
            with open("library.json", "r") as f:
                self.library = json.load(f)
        except FileNotFoundError:
            self.library = []

    def all(self):
        return self.library

    def get(self, id):
        return self.library[id]

    def create(self, data):
        data.pop('csrf_token')
        self.library.append(data)

    def save_all(self):
        with open("library.json", "w") as f:
            json.dump(self.library, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.library[id] = data
        self.save_all()


library = Library()
class Notification:
    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

    def __repr__(self):
        return f"Notification(id: {self.id}, title: {self.title}, description: {self.description})"

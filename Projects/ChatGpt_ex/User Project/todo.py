class Todo:
    def __init__(self, title, priority="normal", deadline=None, category="general"):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.category = category
        self.completed = False

    def complete(self):
        self.completed = True

    def __repr__(self):
        status = "✔" if self.completed else "✗"
        return f"[{status}] {self.title} (우선순위: {self.priority}, 마감: {self.deadline}, 카테고리: {self.category})"

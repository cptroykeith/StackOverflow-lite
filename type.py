class Question:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
        }

    @classmethod
    def get_all(cls):
        # Replace with your actual logic to fetch questions from a data source
        return [
            cls(1, "Sample Question 1", "This is the content of question 1."),
            cls(2, "Sample Question 2", "This is the content of question 2."),
        ]

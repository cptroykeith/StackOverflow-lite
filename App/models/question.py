class Question:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content =content
        
    @classmethod
    def get_all(cls):
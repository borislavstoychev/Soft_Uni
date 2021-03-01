class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)
            
    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [c for c in self.categories if category_id == c.id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [t for t in self.topics if topic_id == t.id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = [d for d in self.documents if document_id == d.id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if category_id == c.id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if topic_id == t.id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [d for d in self.documents if document_id == d.id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [d for d in self.documents if document_id == d.id][0]
        return document

    def __repr__(self):
        documents = list(map(str, self.documents))
        return "\n".join(documents)
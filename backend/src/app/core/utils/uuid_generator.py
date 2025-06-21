import uuid

class UUIDGenerator:
    @staticmethod
    def generate_identifier():
        return str(uuid.uuid4())

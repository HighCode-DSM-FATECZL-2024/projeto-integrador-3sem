from starlette.status import HTTP_409_CONFLICT

class AppException(Exception):
    def __init__(self, message="Application error", status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def to_dict(self):
        return {
            "status": "error",
            "message": self.message
        }

class PasswordsDoNotMatchException(AppException):
    def __init__(self, message="Passwords do not match.", status_code=HTTP_409_CONFLICT):
        super().__init__(message, status_code)

class DataAlreadyExistsException(AppException):
    def __init__(self, message="This data already exists in the database.", status_code=HTTP_409_CONFLICT):
        super().__init__(message, status_code)
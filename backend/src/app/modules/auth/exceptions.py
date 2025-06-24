from starlette.status import HTTP_409_CONFLICT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED

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

class NonExistentEmailException(AppException):
    def __init__(self, message="E-mail does not exist in the database.", status_code=HTTP_404_NOT_FOUND):
        super().__init__(message, status_code)

class InvalidCredentialsException(AppException):
    def __init__(self, message="Invalid user credentials.", status_code=HTTP_401_UNAUTHORIZED):
        super().__init__(message, status_code)
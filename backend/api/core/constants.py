# RESPONSE MESSAGES
INVALID_SCOPE_TOKEN_MSG: str = "Invalid scope for token"
REFRESH_TOKEN_EXP_MSG: str = "Refresh token expired"
INVALID_REFRESH_TOKEN_MSG: str = "Invalid refresh token"
INVALID_TOKEN_MSG: str = "Invalid token"
TOKEN_EXP_MSG: str = "Token expired"
SUCCESS_CREATED_MSG: dict = {"result": True, "message": "Created successfully."}
SUCCESS_UPDATED_MSG: dict = {"result": True, "message": "Updated successfully."}
SUCCESS_DELETED_MSG: dict = {"result": True, "message": "Deleted successfully."}
NOT_FOUND_MSG: str = "Resource not found."
MISSING_PARAMS_MSG: str = "Missing parameter."
INVALID_KEYWORD_MSG: str = "Missing parameter or invalid keyword argument."
INVALID_USERNAME_MSG: str = "Invalid username"
INVALID_PASSWORD_MSG: str = "Invalid password"


# Router Paths
LOGIN_URL = "/login"
SIGNUP_URL = "/signup"
REFRESH_TOKEN_URL = "/refresh_token"
STATIC_FILES_PATH = "/static"

from core.constants import (
    INVALID_REFRESH_TOKEN_MSG,
    INVALID_SCOPE_TOKEN_MSG,
    INVALID_TOKEN_MSG,
    REFRESH_TOKEN_EXP_MSG,
    TOKEN_EXP_MSG,
    INVALID_KEYWORD_MSG,
    MISSING_PARAMS_MSG,
    NOT_FOUND_MSG,
)
from fastapi import HTTPException, status

INVALID_SCOPE_TOKEN = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail=INVALID_SCOPE_TOKEN_MSG
)

INVALID_TOKEN = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail=INVALID_TOKEN_MSG
)

EXPIRED_TOKEN = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail=TOKEN_EXP_MSG
)

REFRESH_TOKEN_EXP = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail=REFRESH_TOKEN_EXP_MSG
)

INVALID_REFRESH_TOKEN = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail=INVALID_REFRESH_TOKEN_MSG
)

NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND_MSG)

MISSING_PARAMS = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail=MISSING_PARAMS_MSG
)


INVALID_KEYWORD = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_KEYWORD_MSG
)


INVALID_REQ_ERROR = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_KEYWORD_MSG
)

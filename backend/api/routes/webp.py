import os
import shutil
from core.auth import Auth
from core.config import API_PREFIX
from fastapi import APIRouter, Security, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from PIL import Image
from pathlib import Path

router = APIRouter(prefix=API_PREFIX)

security = HTTPBearer()
auth = Auth()


@router.post("/converter")
async def convert_image_to_webp(
    file: UploadFile = File(...),
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> JSONResponse:
    token = credentials.credentials
    if auth.decode_token(token):
        with open(f"{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        new_file = await convert_to_webp(Path(f"{file.filename}"))
        os.remove(file.filename)
        return {"filename": f"/static/webp/{new_file}"}


async def convert_to_webp(source):
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(
        f"{os.getcwd()}/static/webp/{destination}", format="webp"
    )  # Convert image to webp

    return destination

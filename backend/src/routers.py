from fastapi import APIRouter, File, UploadFile,  HTTPException
from fastapi.responses import PlainTextResponse, FileResponse
import PIL.Image
import requests
import io
import random
from .utils import (
    ASCIIConverter
)

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello world"}

@router.get("/read-filename")
async def read_filename(file: UploadFile):
    return {"filename": file.name}

@router.post("/get-txt-by-img-file")
async def get_txt_img(file: UploadFile):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image format. Only JPEG and PNG are supported.")
    
    try:
        image = PIL.Image.open(io.BytesIO(await file.read()))
    except Exception as ex:
        raise HTTPException(status_code=404, detail=f"Error processing image: {ex}")
    
    new_image = ASCIIConverter.pixels_to_ascii(ASCIIConverter.grayify(ASCIIConverter.resize_image(image)))
    pixel_count = len(new_image)
    ascii_image = "\n".join(new_image[i:(i+200)] for i in range(0, pixel_count, 200))

     # Save ASCII image to a file
    output_path = f"{file.filename}.txt"
    with open(output_path, "w") as file:
        file.write(ascii_image)

    # Return the file for download
    return FileResponse(path=output_path, filename=output_path, media_type='text/plain')

    # return PlainTextResponse(content=ascii_image)

@router.post("/get-txt-by-img-url")
async def get_txt_img(url: str):
    try:
        request = requests.get(url)
        request.raise_for_status()
        image = PIL.Image.open(io.BytesIO(request.content))
    except Exception as ex:
        raise HTTPException(status_code=404, detail=f"Error processing image: {ex}")
    
    new_image = ASCIIConverter.pixels_to_ascii(ASCIIConverter.grayify(ASCIIConverter.resize_image(image)))
    pixel_count = len(new_image)
    ascii_image = "\n".join(new_image[i:(i+200)] for i in range(0, pixel_count, 200))

     # Save ASCII image to a file
    name = "".join(map(str, [random.randint(0, 10) for i in range(10)]))
    output_path = str(name)+".txt"
    with open(output_path, "w") as file:
        file.write(ascii_image)

    # Return the file for download
    return FileResponse(path=output_path, filename=output_path, media_type='text/plain')
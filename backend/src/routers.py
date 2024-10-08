from fastapi import APIRouter, File, UploadFile,  HTTPException
from fastapi.responses import PlainTextResponse, FileResponse
import PIL.Image
import requests
import io
import random
from .utils import (
    ASCIIConverter
)
from pydantic import BaseModel, ValidationError

router = APIRouter()

class ImageUpload(BaseModel):
    image: str  # Adjust the field type according to your requirement

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
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        image = PIL.Image.open(io.BytesIO(response.content))
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


# @router.post("/get-txt-by-img-url")
# async def get_txt_img(url: str):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # This will raise an error for 4xx and 5xx status codes
#         image = PIL.Image.open(io.BytesIO(response.content))
        
#         # Assuming ASCIIConverter is properly defined elsewhere
#         new_image = ASCIIConverter.pixels_to_ascii(ASCIIConverter.grayify(ASCIIConverter.resize_image(image)))
#         pixel_count = len(new_image)
#         ascii_image = "\n".join(new_image[i:(i+200)] for i in range(0, pixel_count, 200))

#         # Save ASCII image to a file
#         name = "".join(map(str, [random.randint(0, 10) for _ in range(10)]))
#         output_path = f"{name}.txt"
#         with open(output_path, "w") as file:
#             file.write(ascii_image)

#         # Return the file for download
#         return FileResponse(path=output_path, filename=output_path, media_type='text/plain')

#     except requests.exceptions.RequestException as req_ex:
#         raise HTTPException(status_code=400, detail=f"Error fetching the image: {str(req_ex)}")
#     except PIL.UnidentifiedImageError:
#         raise HTTPException(status_code=400, detail="The provided URL does not contain a valid image.")
#     except Exception as ex:
#         raise HTTPException(status_code=500, detail=f"Error processing image: {str(ex)}")
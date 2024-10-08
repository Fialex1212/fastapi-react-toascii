from fastapi import APIRouter, UploadFile,  HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
import io, os, asyncio, requests, random, PIL.Image
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
async def get_txt_img(file: UploadFile, background_tasks: BackgroundTasks):
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
        
    background_tasks.add_task(delete_file_after_delay, output_path, 10)

    # Return the file for download
    return FileResponse(path=output_path, filename=output_path, media_type='text/plain')


@router.post("/get-txt-by-img-url")
async def get_txt_img(url: str, background_tasks: BackgroundTasks):
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
        
    background_tasks.add_task(delete_file_after_delay, output_path, 10)

    # Return the file for download
    return FileResponse(path=output_path, filename=output_path, media_type='text/plain')

async def delete_file_after_delay(file_path: str, delay: int):
    await asyncio.sleep(delay)  # Wait for the specified delay
    if os.path.exists(file_path):
        os.remove(file_path)  # Delete the file
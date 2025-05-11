from fastapi import APIRouter, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from services.ascii_service import process_image_file, process_image_url

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello world"}

@router.get("/read-filename")
async def read_filename(file: UploadFile):
    return {"filename": file.filename}

@router.post("/get-txt-by-img-file")
async def get_txt_img_file(file: UploadFile, background_tasks: BackgroundTasks):
    try:
        output_path = await process_image_file(file, background_tasks)
        return FileResponse(path=output_path, filename=output_path, media_type='text/plain')
    except HTTPException as ex:
        raise ex

@router.post("/get-txt-by-img-url")
async def get_txt_img_url(url: str, background_tasks: BackgroundTasks):
    try:
        output_path = await process_image_url(url, background_tasks)
        return FileResponse(path=output_path, filename=output_path, media_type='text/plain')
    except HTTPException as ex:
        raise ex

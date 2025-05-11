import io, os, asyncio, requests, random
from fastapi import UploadFile, HTTPException, BackgroundTasks
from utils.utils import ASCIIConverter
import PIL.Image


async def process_image_file(
    file: UploadFile, background_tasks: BackgroundTasks
) -> str:
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid image format. Only JPEG and PNG are supported.",
        )

    try:
        image = PIL.Image.open(io.BytesIO(await file.read()))
    except Exception as ex:
        raise HTTPException(status_code=404, detail=f"Error processing image: {ex}")

    return await generate_ascii_file(image, file.filename, background_tasks)


async def process_image_url(url: str, background_tasks: BackgroundTasks) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        image = PIL.Image.open(io.BytesIO(response.content))
    except Exception as ex:
        raise HTTPException(status_code=404, detail=f"Error processing image: {ex}")

    filename = "".join(str(random.randint(0, 9)) for _ in range(10))
    return await generate_ascii_file(image, filename, background_tasks)


async def generate_ascii_file(
    image, filename: str, background_tasks: BackgroundTasks
) -> str:
    new_image = ASCIIConverter.pixels_to_ascii(
        ASCIIConverter.grayify(ASCIIConverter.resize_image(image))
    )
    pixel_count = len(new_image)
    ascii_image = "\n".join(
        new_image[i : (i + 200)] for i in range(0, pixel_count, 200)
    )

    output_path = f"{filename}.txt"
    with open(output_path, "w") as f:
        f.write(ascii_image)

    background_tasks.add_task(delete_file_after_delay, output_path, 10)
    return output_path


async def delete_file_after_delay(file_path: str, delay: int):
    await asyncio.sleep(delay)
    if os.path.exists(file_path):
        os.remove(file_path)

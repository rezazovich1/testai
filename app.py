from fastapi import FastAPI, UploadFile, File
import os, shutil
from typing import List  # 👈 اضافه شده
from analyzer import find_best_resume

app = FastAPI()

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_resumes(files: List[UploadFile] = File(...)):  # 👈 اینجا تغییر داده شده
    saved_files = []
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        saved_files.append(file_path)

    best_resume = find_best_resume(saved_files)
    return {"best_resume": best_resume}

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# enguring upload folder exist 

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# step 2 static file setup 
# url : HTTP://127.0.0.1:8080/FILES/<FILEnAME>
app.mount("/files",StaticFiles(directory=UPLOAD_DIR), name="files")

# step 3 upload file api
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)

    if not filename:
        raise HTTPException(status_code=400, detail="File not selected")
    
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

        return{
            "message":"file Uplaoded successfully",
            "fileName":filename,
            "file_url":f"http://127.0.0.1:8000/files/{filename}"

        }
@app.get("/")
def home():
    return{
        "message":"File Uploaded api Running"
    }
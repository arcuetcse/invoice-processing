uvicorn app:app --reload

The command uvicorn app:app --reload refers to:

app: the file app.py (the Python "module").
app: the object created inside of app.py with the line app = FastAPI().
--reload: make the server restart after code changes. Only use for development.
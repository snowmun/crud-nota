from fastapi import FastAPI
from routes.noteService import router as notes_router
from routes.userService import router as users_router
from routes.labelService import router as label_router

app = FastAPI()

app.include_router(notes_router)
app.include_router(users_router)
app.include_router(label_router)


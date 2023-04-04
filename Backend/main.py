from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.noteService import router as notes_router
from routes.userService import router as users_router
from routes.labelService import router as label_router
from routes.labelNoteService import router as labelNoteService
from routes.typeService import router as typeService

app = FastAPI()

# Configuración de orígenes permitidos para CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://my-app.com",
    "https://my-app.com:8080",
]

# Agregar middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes_router)
app.include_router(users_router)
app.include_router(label_router)
app.include_router(labelNoteService)
app.include_router(typeService)




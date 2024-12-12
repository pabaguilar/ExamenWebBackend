from fastapi import FastAPI
from routes import evento_route, log_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todo
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(log_route.router, prefix="/logs")
app.include_router(evento_route.router, prefix="/eventos")
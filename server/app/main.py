from fastapi import FastAPI
from app.routes import prices
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect (adjust origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register your routes
app.include_router(prices.router, prefix="/api")


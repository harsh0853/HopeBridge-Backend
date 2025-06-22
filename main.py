from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user, donation, request, assignment
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="HopeBridge API",
    description="Donation & Request Management API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router, prefix="/api/user", tags=["User"])
app.include_router(donation.router, prefix="/api/donation", tags=["Donation"])
app.include_router(request.router, prefix="/api/request", tags=["Request"])
app.include_router(assignment.router, prefix="/api/match", tags=["Match"])

@app.get("/")
async def root():
    return {"message": "HopeBridge backend is live!"}

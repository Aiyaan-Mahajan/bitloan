from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import voltage, node

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(voltage.router)
app.include_router(node.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
if __name__ == "__main__":
    # Get the port from the environment variable 'PORT', defaulting to 8000 for local testing
    port = int(os.environ.get("PORT", 8000))
    # Bind to 0.0.0.0 to ensure Railway can route external traffic to the container
    uvicorn.run(app, host="0.0.0.0", port=port)

from fastapi import FastAPI
from routers import router as calls_router
from fastapi.middleware.cors import CORSMiddleware
origins = [ 
    "http://localhost:3000",
    "http://localhost:4000",
    
]
app = FastAPI(
    title="Dummy Phone Calls API",
    description="This API provides simulated phone call data for testing and development purposes. It allows candidates to filter and paginate call data based on specific criteria.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
app.include_router(calls_router,tags=['Calls'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

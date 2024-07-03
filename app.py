from fastapi import FastAPI
import uvicorn
from service_handler import SERVICE_HANDLER
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Service API",
    description="",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    servers=[
        {"url": "http://localhost:6009", "description": "Local Development"},
    ],
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return "Hello World"


@app.get("/start")
async def start(id):
    if SERVICE_HANDLER.start_service(id):
        print("Service Started")
    else:
        return "Error"


@app.get("/stop")
async def stop(id):
    SERVICE_HANDLER.stop_service(id)


@app.get("/restart")
async def restart(id):
    SERVICE_HANDLER.stop_service(id)
    SERVICE_HANDLER.start_service(id)


@app.get("/services")
async def get_services():
    return [{"id": service["id"], "name": service["name"], "status": service["status"]} for service in SERVICE_HANDLER.services]

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=6009)
    except KeyboardInterrupt:
        print("Stopping Server...")

from pathlib import Path
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from Tools.parse_context import parse_context

from LLM.create_response import create_response
from LLM.connect_llm import connect_llm

app = FastAPI()

client, deployment_name = connect_llm()

BASE_DIR = Path(__file__).resolve().parent  # project_root

# Build paths from there
static_dir = BASE_DIR / "UI" / "static"
templates_dir = BASE_DIR / "UI" / "templates"

# Mount static files using the resolved static_dir
app.mount("/static", StaticFiles(directory = str(static_dir)), name="static")

# Tell FastAPI where to find templates
templates = Jinja2Templates(directory = str(templates_dir))

# route to serve chat page
@app.get("/", response_class = HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

# WebSocket route
@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # ADD A CONIDITON TO CHECK IF ITS GENERAL CHAT OR REQUIRES MCP
            data = await websocket.receive_text()
            response = parse_context(data)
            if response == None:
                final_output = data
                bot_response = create_response(client = client, 
                                            deployment_name = deployment_name, 
                                            message = final_output,
                                            found = 0
                )
                await websocket.send_text(bot_response)
            else:
                final_output = str(response)
                await websocket.send_text(final_output)
            print(final_output)
            
            # send back
            
    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port = 8000, reload = True)
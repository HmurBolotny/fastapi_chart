from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import Response
import asyncio
import json




app = FastAPI()
templates = Jinja2Templates(directory="templates")


x = [(7498,14.8), (7498,14.8), (7499,14.9), (7499,14.9), (7500,15), (7500,15), (7501,15.1), (7501,15.1),
         (7502,15.2), (7502,15.2), (7502,15.3), (7503,15.3), (7503,15.3), (7504,15.4)]
y = 123

impoc_hardness = [14.8, 14.8, 14.9, 14.9, 15, 15, 15.1, 15.1, 15.2, 15.2, 15.2, 15.3, 15.3, 15.4]
impoc = [7498, 7498, 7499, 7499, 7500, 7500, 7501, 7501, 7502, 7502, 7502, 7503, 7503, 7504]


def generation():
    print ('generation')
    return ()

def write_db():
    print('write_db')
    return()

def read_db():
    print('read_db')
    return()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> Response:
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/chart-data")
async def chart_data(request: Request) -> StreamingResponse:

    print('chart')
    await asyncio.sleep(1)
    return ()





# logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
# logger = logging.getLogger(__name__)
#
# application = FastAPI()
# templates = Jinja2Templates(directory="templates")
# random.seed()  # Initialize the random number generator
#
#
# @application.get("/", response_class=HTMLResponse)
# async def index(request: Request) -> Response:
#     return templates.TemplateResponse("index.html", {"request": request})
#
#
# async def generate_random_data(request: Request) -> Iterator[str]:
#     """
#     Generates random value between 0 and 100
#
#     :return: String containing current timestamp (YYYY-mm-dd HH:MM:SS) and randomly generated data.
#     """
#     client_ip = request.client.host
#
#     logger.info("Client %s connected", client_ip)
#
#     while True:
#         json_data = json.dumps(
#             {
#                 "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "value": random.random() * 100,
#             }
#         )
#         yield f"data:{json_data}\n\n"
#         await asyncio.sleep(1)
#
#
# @application.get("/chart-data")
# async def chart_data(request: Request) -> StreamingResponse:
#     response = StreamingResponse(generate_random_data(request), media_type="text/event-stream")
#     response.headers["Cache-Control"] = "no-cache"
#     response.headers["X-Accel-Buffering"] = "no"
#     return response

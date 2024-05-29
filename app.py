import random
from typing import Iterator, Annotated

from queries.orm import create_tables, SyncOrm #, AsyncORM

from fastapi import FastAPI, Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import Response
import asyncio
import json
# from IMPOK.queries import (
#     create_tables,
#     delete_tables,
#     SyncRepo
# )


# create_tables()


SyncOrm.create_tables()
SyncOrm.mark_descr_insert("test_name_2", "")         #test_name_2"
SyncOrm.mark_descr_update(1, 'name3', 'descr3')
SyncOrm.mark_descr_insert("test_name_4", "12345")         #test_name_2"
SyncOrm.mark_descr_insert("test_name_5", "123")         #test_name_2"
SyncOrm.mark_descr_select()
SyncOrm.mark_coeff_insert(1, 22, 50, 41)
SyncOrm.mark_coeff_update(1, 2, 3, 4)






# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
#
# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}
#
#
# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request) -> Response:
#     return templates.TemplateResponse("index.html", {"request": request})
#
#
# @app.get("/chart-data")
# async def chart_data(request: Request) -> StreamingResponse:
#     delete_tables()
#     create_tables()
#     response = StreamingResponse(select_last_data(request), media_type="text/event-stream")
#     response.headers["Cache-Control"] = "no-cache"
#     response.headers["X-Accel-Buffering"] = "no"
#     return response
#

# repo = SyncRepo
#
#
# # async def database_worker_main(request) -> Iterator[str]:
# #     while True:
# #         generate_random_data()
# #         select_last_val(request)
# #         await asyncio.sleep(1)
#
#
# async def select_last_data(request: Request) -> Iterator[str]:
#     while True:
#         repo.insert_val(repo, generate_random_data())
#         # insert_val(generate_random_data())
#         data = repo.select_last_val(repo)
#         # data = select_last_val()
#         title = ['id', 'impoc', 'hardness']
#         data2 = [
#             dict(zip(title, list(row))) for row in data
#         ]
#         json_data = json.dumps(data2[0])
#         yield f"data:{json_data}\n\n"
#         await asyncio.sleep(1)
#
#
# def generate_random_data():
#     data = {
#         "impoc": round(random.uniform(14, 18), 2),
#         "hardness": random.randint(7500, 7600),
#     }
#     return data
#
#
# async def main():
#     await AsyncORM.create_tables()
#
#
#
# # SyncOrm.create_tables()
#
# # if __name__ == "__main__":
# #     uvicorn.run(app, host="0.0.0.0", port=8000)




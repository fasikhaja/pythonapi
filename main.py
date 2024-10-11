import sys

import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from routers.cpic_router import router

app = FastAPI(title="equite")
app.include_router(router)

add_pagination(app)


@app.get("/")
async def root():
    return {"*************** EQUITE! ***************"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8089)
# uvicorn main:app --reload

import requests

from DFA import getFilterByData
from main import app
from sanic import response, Request


@app.route("/toTrain")
async def getTrain(request: Request):
    url = request.headers.get("url")
    type = request.headers.get("type")
    data = requests.get(url).text
    model = getFilterByData(data, type)


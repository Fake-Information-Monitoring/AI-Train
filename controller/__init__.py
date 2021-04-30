import requests
from sanic import Blueprint
from sanic import Request, json

bp = Blueprint('my_blueprint')

import dill as pickle

from DFA import getFilterByData


async def train(redis, text, uuid, types):
    model = getFilterByData(text, types)
    model = pickle.dumps(model)
    await redis.set(uuid + 'model', model)
    requests.post('http://127.0.0.1:8080/v1/upload/addTrainModel', headers={
        'uuid': uuid,
        'type': types
    }, files={'file': model})


@bp.post("/toTrain")
async def getTrain(request: Request):
    url = request.form.get("url")
    types = request.form.get("type")
    uuid = request.form.get("uuid")
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.text
    await train(request.app.redis, data, uuid, types)
    return json({
        "code": 200,
        "success": True,
        "data": "success"
    })

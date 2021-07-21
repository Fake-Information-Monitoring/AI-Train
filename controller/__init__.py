import requests
from sanic import Blueprint
from sanic.response import json

import DFA

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
async def getTrain(request):
    url = request.form.get("url")
    types = request.form.get("type")
    uuid = request.form.get("uuid")
    response = requests.get(url)
    response.encoding = 'utf-8'
    data = response.text
    await train(request.app.redis, data, uuid, types)
    return json({
            "code": 200,
            "success": False,
            "data": {
                "uuid":uuid
            },
            "isFake":False
        })

@bp.post("/VerifyDIYModel")
async def verifyDIYModel(request):
    redis = request.app.redis
    uuid = request.form.get("uuid")
    text = request.form.get("text")
    model = await redis.get(uuid + 'model')
    model:DFA.DFAFilter = pickle.loads(model)
    text, words = model.filter(text)
    isFake = True if(len(words)> 0) else False
    data = {}
    data['DIYModel'] = words
    return json({
            "code": 200,
            "success": True,
            "isFake": isFake,
            "text": text,
            "data": data
        })


@bp.post("/")
async def handler(request):
    transport, protocol = await request.app.amqp.connect()

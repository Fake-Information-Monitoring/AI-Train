from sanic import Sanic

app = Sanic("app")
app.config.update({
    'REDIS': {
        'address': ('127.0.0.1', 6379)
    },
    "AMQP_USERNAME": "guest",
    "AMQP_PASSWORD": "guest",
    "AMQP_HOST": "localhost",
    "AMQP_PORT": 5672,
    "AMQP_VIRTUAL_HOST": "vhost",
    "AMQP_USING_SSL": False,
})
from sanic_redis import SanicRedis

redis = SanicRedis(app, config_name='REDIS')
from controller import bp

app.blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)

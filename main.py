from sanic import Sanic

app = Sanic("app")
app.config.update(
    {
        'REDIS': {
            'address': ('127.0.0.1', 6379)
        }
    }

)
from sanic_redis import SanicRedis

redis = SanicRedis(app, config_name='REDIS')
from controller import bp

app.blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)

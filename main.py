# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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

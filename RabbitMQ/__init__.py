from sanic_amqp_ext import AmqpWorker


class CustomWorker(AmqpWorker):

    async def run(self, *args, **kwargs):
        transport, protocol = await self.connect()  # create a new connection
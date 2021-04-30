import asyncio_redis

from config import REDIS_CONFIG


class RedisConf:
    _pool = None

    async def get_redis_pool(self):
        if self._pool is None:
            self._pool = await asyncio_redis.Pool.create(
                host=REDIS_CONFIG['host'], port=REDIS_CONFIG['port'],
                password=REDIS_CONFIG.get('password'), poolsize=10
            )
        return self._pool

    async def close(self):
        if self._pool:
            self._pool.close()

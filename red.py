import redis

red = redis.Redis(
     host='redis-14209.c9.us-east-1-2.ec2.cloud.redislabs.com',
     port=14209,
     password='5E5ldYa3yaHwajZMtfgHDsDuSOnXfHhG'
)
red.set('var1', 'value1') # записываем в кеш строку "value1"
print(red.get('var1')) # считываем из кэша данные

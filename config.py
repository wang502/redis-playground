import os
import urlparse
import redis
url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
print "connected successfully"
r = redis.Redis(host=url.hostname, port=url.port, password=url.password)

# pip install python-geohash
# pip install numpy
import numpy as np
import geohash

NUM_POINTS = 500_000

longitude = np.random.rand(NUM_POINTS) * 360 - 180
latitude = np.random.rand(NUM_POINTS) * 180 - 90
@np.vectorize 
def geohashEncode(longitude, latitude, precision=3):
    return geohash.encode(latitude, longitude, precision)
geohash = geohashEncode(longitude, latitude)

data = b','.join([b'(' + b','.join(map(lambda x: repr(x).encode(),(i,)+tup)) + b')' for i,tup in enumerate(zip(longitude, latitude, geohash))])

with open('floats.bin', 'wb') as f: 
    f.write(data)

csv = '\n'.join([','.join(map(lambda x: repr(x),(i,)+tup)) for i,tup in enumerate(zip(longitude, latitude, geohash))])
with open('floats.csv', 'w') as f: 
    f.write(csv)

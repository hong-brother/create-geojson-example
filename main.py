# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import log4p
import os
from geojson import Feature, Point, Polygon,  FeatureCollection

print("dir - " + os.getcwd() + '/config/log4p.json')
logger = log4p.GetLogger(__name__, config=os.getcwd() + '/config/log4p.json')
log = logger.logger
customPoint = Point((23.532, -63.12))
crs = {
    "type": "name",
    "properties": {
        "name": "EPSG:3857"
    }
}

#http://www.gisdeveloper.co.kr/?p=8002
def createGeoJson():
    bbox = Feature(geometry=customPoint,
                   properties={
                       "name": "bbox",
                       "projectId": "60077eec-2287-4381-96bb-4ca4b424d9bd"
                   })
    inference1 = Feature(geometry=customPoint,
                         properties={
                             "name": "inference",
                             "class": 1,
                             "canvas": [[123, 123], [123, 123]],
                             "rasterId": 0
                         })
    inference2 = Feature(geometry=customPoint,
                         properties={
                             "name": "inference",
                             "class": 1,
                             "canvas": [[123, 123], [123, 123]],
                             "rasterId": 0
                         })
    return FeatureCollection([bbox, inference1, inference2], crs=crs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = createGeoJson()
    log.info(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

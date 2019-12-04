import base64
import json
from PIL import Image
from io import BytesIO


filename = sys.argv[1]

with open(filename, "r") as response_file:
    response_data = json.loads(response_file.read())

index = 0
for image in response_data['images']:
    index++
    with open("simulation_00" + index, "wb") as im:
        im.write(base64.decodebytes(image))

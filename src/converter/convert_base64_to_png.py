import base64
import json
from PIL import Image
from io import BytesIO
import sys

filename = sys.argv[1]

with open(filename, "r") as response_file:
    response_data = json.loads(response_file.read())

index = 0
for image in response_data['images']:
    index = index + 1
    im = Image.open(BytesIO(base64.b64decode(image)))
    im.save('simulation_' + str(index) + '.png', 'PNG')

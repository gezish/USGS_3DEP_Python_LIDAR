import logging
from typing import Tuple
import pdal
import json
import sys, os

with open('pipeline.json', 'r') as json_file:
        json_obj = json.load(json_file)

print(json_obj)

pipeline = pdal.Pipeline(json.dumps(json_obj)).execute()
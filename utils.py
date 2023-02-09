import json
import os
from datetime import datetime, timedelta
import pprint

def pp(var, name=None):
    if name:
        print(f"{{ {name} }}:")
    pprint.pprint(var)

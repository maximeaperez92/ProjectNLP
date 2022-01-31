import numpy as np
import json


def extract_genre(val):
    if type(val) is str:
        # print(f"val: {json.loads(val)}, type: {type(val)}")
        return list(json.loads(val).values())
    else:
        return ''


def remove_first_withespace(summary: str):
    if summary[0] == " ":
        return summary[1:]
    else:
        return summary

import json
from functools import wraps
import time

from ai21.data_types import AI21StudioResponse


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def build_ai21studio_response(func):
    @wraps(func)
    def measure_execution_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        ai21_studio_response = AI21StudioResponse(data=result[1], headers=result[0], execution_time=total_time)
        return ai21_studio_response

    return measure_execution_time_wrapper

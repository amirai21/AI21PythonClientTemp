import json
from functools import wraps
import time


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))


def measure_execution_time(func):
    @wraps(func)
    def measure_execution_time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        return total_time, result

    return measure_execution_time_wrapper

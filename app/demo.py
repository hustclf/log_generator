import json
from datetime import datetime
import time


class Format(object):
    def __init__(self):
        pass

    @staticmethod
    def run(log, index, total):
        timestamp = int(time.mktime(log['time_local']))
        log['date'] = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        del log['time_local']
        return json.dumps(log)
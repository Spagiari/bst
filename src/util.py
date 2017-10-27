import time
from datetime import datetime

EP = datetime.fromtimestamp(0)

def old_date_to_float(d):
    if d == None:
        DT = datetime.fromtimestamp(0)
    else:
        try:
            DT = datetime.strptime(d, '%Y%m%d%H%M%S.%f0')
        except:
            DT = datetime.fromtimestamp(0)
    return (DT - EP).total_seconds()

def date_to_float(d):
    if d == None or d = 0.0:
        return (datetime.fromtimestamp(0) - EP).total_seconds()
    return datetime.strptime(d, "%Y%m%d%H%M%S.%f0").timestamp()


def float_to_date(fl):
    return datetime.fromtimestamp(fl).strftime('%Y%m%d%H%M%S.%f0')

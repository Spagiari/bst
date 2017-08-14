from datetime import datetime

EP = datetime(2000,1,1)

def date_to_float(d):
    if d == None:
        DT = datetime.now()
    else:
        DT = datetime.strptime(d, '%Y%m%d%H%M%S.%f0')
    return (DT - EP).total_seconds()


from datetime import datetime

EP = datetime.fromtimestamp(0)

def date_to_float(d):
    if d == None:
        DT = datetime.fromtimestamp(1)
    else:
        try:
            DT = datetime.strptime(d, '%Y%m%d%H%M%S.%f0')
        except:
            DT = datetime.fromtimestamp(1)
    return (DT - EP).total_seconds()

def float_to_date(fl):
    return datetime.fromtimestamp(fl).strftime('%Y%m%d%H%M%S.%f0')

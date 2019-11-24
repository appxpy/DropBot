from datetime import datetime
def now():
    now = datetime.now()
    return  now.strftime("%X")
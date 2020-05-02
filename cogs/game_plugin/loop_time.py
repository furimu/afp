from datetime import datetime
from utils.date import *

load_ousama = load('ousama_')
def hour_check(vc: str):
    if not load_ousama[vc].get('hour'):
        return False
    if int(load_ousama[vc]['hour']) - datetime.now().hour== 0:
        return True

    else:
        return False


def mintue_check(vc: str):
    if not load_ousama[vc].get('hour'):
        return False

    if int(load_ousama[vc]['minute']) - datetime.now().minute== 5:
        return True

    elif int(load_ousama[vc]['minute']) == 00 and datetime.now().minute == 55:
        return True

    else:
        return False
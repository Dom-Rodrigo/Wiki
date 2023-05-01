import random
from . import util

def sort_random(request):
    print(request)
    return {"random": f"/{random.choice(util.list_entries())}"}
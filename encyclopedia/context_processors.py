import random
from . import util


def sort_random(request):
    return {"random": random.choice(util.list_entries())}
import sys
from time import sleep
from random import random

LINES = 10
WAIT = 0.5
OUT_STR = "Train Loss: {} Validation Loss: {} D(x): {} G(D(x)): {}"

for k in range(LINES):
    print(OUT_STR.format(random(), random(), random(), random()))
    sys.stdout.flush()
    sleep(WAIT)


from time import sleep
from random import random

LINES = 10
WAIT = 1
OUT_STR = "Train Loss: {} Validation Loss: {} D(x): {} G(D(x)): {} Train Acc: {} Validation Acc: {}"

for k in range(LINES):
    print(OUT_STR.format(random(), random(), random(), random(), random(), random()))
    sleep(WAIT)


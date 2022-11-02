import numpy as np
import time
with open("frames.txt", "r") as f:
    lines = f.readlines()

for i,v in enumerate(lines):
    lines[i] = v.replace("\\n","\n")
    print(f"Converting frame {i}")
for i in lines:
    print(i)
    time.sleep(1/30)

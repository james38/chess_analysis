import sys
#import os
import subprocess
import shlex

print('Python version:', sys.version)

lc0_call = '~/lc0/build/release/lc0 --backend=cudnn-fp16 --verbose-move-stats'

with open('inputs.txt') as f:
    instructions = f.read().splitlines()
evals = open('evals.txt')
# this works to run leela, though it is an old method
#  as per Python docs on the subprocess module
#  https://docs.python.org/3/library/subprocess.html
#os.system(lc0_call)

# "If shell is True, it is recommended to pass
#  args as a string rather than as a sequence."
proc = subprocess.Popen(
    args=shlex.split(shlex.quote(lc0_call)),
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)

# default encoding is 'utf-8'
for instruction in instructions:
    proc.stdin.write(f"{instruction}\n".encode())
    proc.stdin.flush()

try:
    outs, errs = proc.communicate(timeout=120)
except Exception:
    proc.kill()
    outs, errs = proc.communicate()

print(outs)
print(errs)

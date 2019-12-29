import sys
#import os
import subprocess
import shlex

print('Python version:', sys.version)

lc0_call = '~/lc0/build/release/lc0 --backend=cudnn-fp16 --verbose-move-stats'
instructions = open('inputs.txt')
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
    stdin=instructions,
    stdout=evals,
    #stderr=subprocess.STDOUT
)
try:
    outs, errs = proc.communicate(timeout=120)
except Exception:
    proc.kill()
    outs, errs = proc.communicate()

print(outs)
print(errs)

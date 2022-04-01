from __future__ import division
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("python-Levenshtein")
import Levenshtein as lstn

def cer(gt, prediction):
    cer_s, cer_i, cer_d, cer_n = 0, 0, 0, 0.

    arr = lstn.editops(gt, prediction) # update
    for item in arr:
        if item[0] == 'insert':
            cer_i += 1
        elif item[0] == 'delete':
            cer_d += 1
        else:
            cer_s += 1
    cer_n = len(gt)
    return (cer_s + cer_i + cer_d) / cer_n
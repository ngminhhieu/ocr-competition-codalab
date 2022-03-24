from __future__ import division
import argparse
import Levenshtein as lstn
def levenshtein(u, v):
    prev = None
    curr = [0] + list(range(1, len(v) + 1))
    # Operations: (SUB, DEL, INS)
    prev_ops = None
    curr_ops = [(0, 0, i) for i in range(len(v) + 1)]
    for x in range(1, len(u) + 1):
        prev, curr = curr, [x] + ([None] * len(v))
        prev_ops, curr_ops = curr_ops, [(0, x, 0)] + ([None] * len(v))
        for y in range(1, len(v) + 1):
            delcost = prev[y] + 1
            addcost = curr[y - 1] + 1
            subcost = prev[y - 1] + int(u[x - 1] != v[y - 1])
            curr[y] = min(subcost, delcost, addcost)
            if curr[y] == subcost:
                (n_s, n_d, n_i) = prev_ops[y - 1]
                curr_ops[y] = (n_s + int(u[x - 1] != v[y - 1]), n_d, n_i)
            elif curr[y] == delcost:
                (n_s, n_d, n_i) = prev_ops[y]
                curr_ops[y] = (n_s, n_d + 1, n_i)
            else:
                (n_s, n_d, n_i) = curr_ops[y - 1]
                curr_ops[y] = (n_s, n_d, n_i + 1)
    return curr[len(v)], curr_ops[len(v)]



def cer(gt, prediction):
    cer_s, cer_i, cer_d, cer_n = 0, 0, 0, 0.

    arr = lstn.editops(gt, prediction) # update
    # print(arr)
    for item in arr:
        if item[0] == 'insert':
            cer_i += 1
        elif item[0] == 'delete':
            cer_d += 1
        else:
            cer_s += 1
    cer_n = len(gt)
        
    # for n in range(len(gt)):
    #     _, (s, i, d) = levenshtein(gt[n], prediction[n])
    #     cer_s += s
    #     cer_i += i
    #     cer_d += d
    #     cer_n += len(gt[n])
    return (cer_s + cer_i + cer_d) / cer_n
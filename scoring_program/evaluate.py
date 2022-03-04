from numpy import genfromtxt

import os
import sys

from sklearn.metrics import roc_auc_score

if __name__ == "__main__":
    [_, input_dir, output_dir] = sys.argv
    submission_dir = os.path.join(input_dir, 'res')
    truth_dir = os.path.join(input_dir, 'ref')

    ground_truth = genfromtxt(os.path.join(truth_dir, 'ground_truth.csv'), delimiter=',')[:, 1]
    ground_truth = ground_truth.astype('int')

    submission = genfromtxt(os.path.join(submission_dir, 'results.csv'), delimiter=',')[:, 1]

    roc = roc_auc_score(ground_truth, submission)

    with open(os.path.join(output_dir, 'scores.txt'), 'w') as output_file:
        output_file.write("ROC: {:f}".format(roc))

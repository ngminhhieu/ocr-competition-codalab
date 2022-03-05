
import os
import sys
import pandas as pd
import subprocess
import rrc_evaluation_funcs
from script import default_evaluation_params, validate_data, evaluate_method
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('jiwer')
import jiwer

if __name__ == "__main__":
    [_, input_dir, output_dir] = sys.argv
    submission_dir = os.path.join(input_dir, 'res')
    truth_dir = os.path.join(input_dir, 'ref')

    # ground_truth_path = os.path.join(truth_dir, 'ground_truth.txt')
    # submission_path = os.path.join(submission_dir, 'results.txt')

    # ground_truth = pd.read_csv(ground_truth_path, sep=',', header=None, names=['x1','y1','x2','y2','x3','y3', 'x4', 'y4', 'label'])
    # submission = pd.read_csv(submission_path, sep=',', header=None, names=['x1','y1','x2','y2','x3','y3', 'x4', 'y4', 'label'])
    # cer = jiwer.cer(list(ground_truth['label']), list(submission['label']))
    # f1 = None
    res_dict = rrc_evaluation_funcs.main_evaluation({'g': '{}/gt_IC15.zip'.format(truth_dir), 's': '{}/gt_IC15.zip'.format(submission_dir)}, default_evaluation_params, validate_data, evaluate_method)
    print(res_dict['method'])
    with open(os.path.join(output_dir, 'scores.txt'), 'w') as output_file:
        output_file.write("CER: {:f}\n".format(round(res_dict['method']['cer'],6)))
        output_file.write("F1: {:f}".format(round(res_dict['method']['hmean'],6)))
    

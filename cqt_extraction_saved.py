import essentia.standard as standard
import numpy as np
import multiprocessing as mp
import tqdm
import glob
import os
import os.path as osp
import deepdish as dd
import pickle


if __name__ == "__main__":
    feat_dir = '/mnt/dataset/public/coversbr/features_cqt'

    files_saved_list = glob.glob(f"{feat_dir}/*/*.h5")

    if osp.isfile('file_saved_list.pkl'):
        with open('file_saved_list.pkl', 'rb') as f:
            old_list = pickle.load(f)
        files_saved_list.extend(old_list)

    with open('file_saved_list.pkl', 'wb') as f:
        pickle.dump(files_saved_list, f)


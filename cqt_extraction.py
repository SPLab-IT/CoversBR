import essentia.standard as standard
import numpy as np
import multiprocessing as mp
import tqdm
import glob
import os
import os.path as osp
import deepdish as dd
import pickle

def extract_and_save(src, dst):
    kwargs = {
        'inputSize': 4096,
        'minFrequency': 32.7,
        'maxFrequency': 4000,
        'binsPerOctave': 12,
        'sampleRate': 22050,
        'rasterize': 'full',
        'phaseMode': 'global',
        'gamma': 0,
        'normalize': 'impulse',
        'window': 'hannnsgcq',
    }

    x = standard.MonoLoader(filename=src, sampleRate=kwargs['sampleRate'])()
    CQStand = standard.NSGConstantQ(**kwargs)

    constantq, constantqdc, constantqnf = CQStand(x)


    out_dict = dict()

    out_dict["NSGConstantQ"] = constantq

    path_audio = src.split('/')
    work_id = path_audio[-2]
    track_id = path_audio[-1]
    track_id = track_id.split('.ogg')[0]

    out_dict['track_id'] = track_id
    out_dict['label'] = work_id

    out_dict['params'] = kwargs

    if not osp.isdir(osp.dirname(dst)):
        os.mkdir(osp.dirname(dst))

    dd.io.save(dst, out_dict)
    #with open(dst, 'wb') as f:
    #    np.save(f, constantq)


if __name__ == "__main__":
    root = "/mnt/dev/dirceusilva/dados/Cover/CoversBR/Audios"
    feat_dir = '/mnt/dataset/public/coversbr/features_cqt'
    num_proc = 96
    fn_list = glob.glob(f"{root}/*/*.ogg")
    fn_list.sort()

    pool = mp.Pool() #num_proc)
    pbar = tqdm.tqdm(total=len(fn_list))

    files_saved_list = []
    if osp.isfile('file_saved.pkl'):
        with open('file_saved.pkl', 'rb') as f:
            files_saved_list = pickle.load(f)

    def update_pbar(*a):
        pbar.update()

    for fn in fn_list:
        src = fn
        path_audio = fn.split('/')
        work_id = path_audio[-2]
        track_id = path_audio[-1]
        track_id = track_id.split('.ogg')[0]
        dst = f"{feat_dir}/{work_id}/{track_id}.h5"

        if not osp.isfile(dst) and not (dst in infiles_saved_list): ## for the halt recovering
            pool.apply_async(extract_and_save, (src, dst), callback=update_pbar)
    pool.close()
    pool.join()
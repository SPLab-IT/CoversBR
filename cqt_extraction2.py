import essentia.standard as standard
import numpy as np
import multiprocessing as mp
import tqdm
import glob
import os
import os.path as osp
import deepdish as dd
import psutil


def process_group(srcdir, fileout):

    def extract(file):
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

        x = standard.MonoLoader(filename=file, sampleRate=kwargs['sampleRate'])()
        CQStand = standard.NSGConstantQ(**kwargs)

        constantq, _, _ = CQStand(x)

        return constantq, kwargs

    files = glob.glob(os.path.join(srcdir, "*.ogg"))

    out_dict = dict()

    for fn in files:
        path_audio = fn.split('/')

        track_id = path_audio[-1]
        track_id = track_id.split('.ogg')[0]

        cqt, params = extract(fn)

        out_dict[track_id] = dict()
        out_dict[track_id]["NSGConstantQ"] = cqt
        out_dict[track_id]['track_id'] = track_id
        out_dict[track_id]['label'] = work_id

        out_dict['params'] = params

    if not osp.isdir(osp.dirname(fileout)):
        os.makedirs(osp.dirname(fileout))

    dd.io.save(fileout, out_dict, compression=('zlib', 9))

if __name__ == "__main__":
    root = "/mnt/dev/dirceusilva/dados/Cover/CoversBR/Audios"
    feat_dir = '/mnt/dataset/public/coversbr/features_cqt'

    # fn_list = glob.glob(f"{root}/*/*.ogg")
    gp_list = glob.glob(f"{root}/*/")

    parallel = True
    num_cpus = psutil.cpu_count(logical=False)

    pbar = tqdm.tqdm(total=len(gp_list))

    def update_pbar(*a):
        pbar.update()

    if parallel:
        pool = mp.Pool(num_cpus)  # num_proc)

        for group_name in gp_list[:1]:

            path_audio = group_name.split('/')
            work_id = path_audio[-2]

            dst = osp.join(feat_dir, work_id, work_id + ".h5")
            print(dst)

            if not osp.isfile(dst):  ## for the halt recovering
                pool.apply_async(process_group, (group_name, dst), callback=update_pbar)

            pool.close()
            pool.join()
    else:
        for group_name in gp_list[:1]:

            path_audio = group_name.split('/')
            work_id = path_audio[-2]

            dst = osp.join(feat_dir, work_id, work_id + ".h5")
            print(dst)

            process_group(group_name, dst)
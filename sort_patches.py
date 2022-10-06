import glob
import shutil
import os

listaimmagini=glob.glob("/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/dsmil-wsi/tcga-download/lung/*/*.svs")
dest="/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/datasets/LUNG"

for img in listaimmagini:
    name=img.split(os.sep)[-1]
    shutil.move(img,os.path.join(dest,name))

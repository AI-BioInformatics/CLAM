import pandas as pd
import numpy as np
import glob
import os
root="/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/patches/lung2/images/TCGA*/*/*.jpg"
listawsi= glob.glob(os.path.join(root,"*"))
df =pd.read_csv("TEST_ID.csv")
#for tuple in df.values:
    #name,label=tuple
    #name=os.path.basename(img)

    #newname=name.split(".")[0]
    #os.rename(os.path.join(root,name),os.path.join(root,"test"+name+"_"+str(label)))

pd.DataFrame(glob.glob(root)).to_csv("training_lung_2.csv")
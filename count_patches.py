import glob
import os
import pandas as pd

path= "/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/patches/CLAM/patches"

#training
#normal

normal_patches_training=glob.glob(os.path.join(path,"normal","normal_*","0","*"))
slideids=[path.split(os.sep)[-3] for path in normal_patches_training]
df_training1=pd.DataFrame({"path":normal_patches_training,"label":0,"slide_id":slideids})



tumor_patches_training=glob.glob(os.path.join(path,"tumor","tumor_*","0","*"))
slideids=[path.split(os.sep)[-3] for path in tumor_patches_training]
df_training2=pd.DataFrame({"path":tumor_patches_training,"label":1,"slide_id":slideids})

df3= df_training1.append(df_training2)
df3.to_csv("/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/patches/CLAM/training.csv")

tumor_patches_test=glob.glob(os.path.join(path,"tumor","test_*","0","*"))
slideids=[path.split(os.sep)[-3] for path in tumor_patches_test]
df_training1=pd.DataFrame({"path":tumor_patches_test,"label":1,"slide_id":slideids})



normal_patches_test=glob.glob(os.path.join(path,"normal","test_*","0","*"))
slideids=[path.split(os.sep)[-3] for path in normal_patches_test]
df_training2=pd.DataFrame({"path":normal_patches_test,"label":0,"slide_id":slideids})

df3= df_training1.append(df_training2)
df3.to_csv("/mnt/beegfs/work/H2020DeciderFicarra/gbontempo/patches/CLAM/test.csv")

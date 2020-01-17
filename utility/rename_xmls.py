import glob
import os
from data import path as data_path

if __name__ == '__main__':
    filenames = glob.glob(data_path.get() + "/images/train/" + "*.xml")
    count = 0

    for filename in filenames:
        print("filename before renamimg", filename)
        os.rename(filename,str(count)+".xml")
        print("filename after renamimg", filename)
        count +=1
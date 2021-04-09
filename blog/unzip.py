#!/usr/bin/env python3
import sys
from zipfile import ZipFile

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Uso incorreto")
        exit(1);
    zip_file = sys.argv[1]
    pzf = ZipFile(zip_file)
    pzf.extractall(sys.argv[2])

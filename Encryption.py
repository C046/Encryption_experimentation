# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 16:40:34 2023

@author: hadaw
"""

from cryptography.fernet import Fernet
import numpy as np
import os


def _list_dir(path):
    file_path = [os.path.join(path,file) for file in os.listdir(path)]    
    print(file_path)
    return file_path

# dirs = _list_dir("D:\Data")
# for i in dirs:
#     if 'primes' in i:
#         print("True")
        
def _encrypt_file(filepath):
    file_data = open(filepath,'rb').read()
    key = Fernet.generate_key()
    
    try:    
        open(filepath, 'wb').write(Fernet(key).encrypt(file_data))
    
    except Exception as E:
        print(E)
        del E
    
    
    try:
        open(f"F:\CIA_Application\KEY-{np.random.randint(0,10000)}-MyLINK-trackingnumber.key", 'wb').write(key)
    
    except Exception as E:
        print(E)
        del E
        

def _decrypt_file(filepath, keylocation):
    dirs = _list_dir(keylocation)
    d = []
    for directories in dirs:
        if 'KEY-' in directories:
            try:

                key = open(directories, "rb").read()
                file_data = open(filepath, 'rb').read()
    
                try:
                    open(filepath, 'wb').write(Fernet(key).decrypt(file_data))
                    os.remove(directories)
    
                except Exception as statement:
                    statement = print("\n Write unsuccessful \n x \n . \n .. \n Reverting changes..")
                    del statement
                    try:
            
                        open(filepath, 'wb').write(file_data)
        
                    except Exception as E:
                        print(E)
                        del E
            
            except Exception:
                print("Tried Unsuccessful key.")
    # with open(filepath,"wb") as File:  
    #     try:    
    #         File.write(Fernet(key).decrypt(file_data))
    #     except Exception as statement:
    #         statement = print("Write Unsuccessful")
    #         File.write(file_data)
    #         del statement 
    
    # # Close the File
    # File.close()

    
    # del File, filepath

    
_encrypt_file("F:\CIA_Application\myLinkExportedData-2023-01-06-06-11-42.json")
_encrypt_file("F:\CIA_Application\MyLINK-trackingnumber.txt")
# _decrypt_file("F:\CIA_Application\MyLINK-trackingnumber.txt", "F:\CIA_Application")
# _decrypt_file("F:\CIA_Application\myLinkExportedData-2023-01-06-06-11-42.json", "F:\CIA_Application")

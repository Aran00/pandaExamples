__author__ = 'ryu'

import pandas as pd


class BinaryData:
    def __init__(self):
        self.frame = pd.read_csv('ch06/ex1.csv')
        pass

    def use_pickle(self):
        pickle_path = 'ch06/frame_pickle'
        self.frame.to_pickle(pickle_path)
        frame_pickle = pd.read_pickle(pickle_path)
        print frame_pickle

    def use_hdf5(self):
        store = pd.HDFStore('mydata.h5')
        store['obj1'] = self.frame
        store['obj1_col'] = self.frame['a']
        print store, store['obj1']

    def read_xls(self):
        '''Not important currently'''
        pass

BinaryData().use_pickle()

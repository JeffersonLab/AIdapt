# handle imput file and get it to numpy array

import numpy as np
import time


class DataManager:

    def __init__(self, file):
        
        self.file = file
    
    def get_numpy_array(self):
        if self.file.endswith('.npy'):
        
            print('Data loaded')
            print('Applying fiducial cuts')
        
            return np.load(self.file)
        
        elif self.file.endswith('.zzz') or self.file.endswith('.txt'):
        
            print('Getting numpy array from .txt file data')
            array = self._get_numpy_array_from_zzz() 
            print('Applying fiducial cuts')
        
            return array


    # Private Methods

    def _get_numpy_array_from_zzz(self):
        
        output_list = []
        
        with open(self.file) as f:
            all_lines = f.readlines()
        
        new_row = []
        
        for line in all_lines:
            for entry in line.split(" "):
                try: 
                    new_row.append(float(entry))
                except ValueError:
                    pass
            
            if len(new_row) == 14:
                output_list.append(new_row)
                new_row = []

        return np.array(output_list)


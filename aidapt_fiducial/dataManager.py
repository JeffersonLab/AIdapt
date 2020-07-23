# handle imput file and get it to numpy array

import numpy as np
import time

# with open('/media/tylerviducic/Elements/aidapt/data/recon/twopi_ppip.10.zzz') as f:
#     all_lines = f.readlines()

# for i in range(10):
#     print(all_lines[i])

class DataManager:

    def __init__(self, file):
        self.file = file
    
    def get_numpy_array(self):
        if self.file.endswith('.npy'):
            return np.load(self.file)
        elif self.file.endswith('.zzz') or self.file.endswith('.txt'):
            return self._get_numpy_array_from_zzz()


    # Private Methods

    def _get_numpy_array_from_zzz(self):
        output_list = []
        
        with open(self.file) as f:
            all_lines = f.readlines()
        
        new_row = []
        start = time.time()
        for i in range(len(all_lines)):
        
            for entry in all_lines[i].split(" "):
                try: 
                    new_row.append(float(entry))
                except ValueError:
                    pass
            if (i + 1) % 5 == 0:
                output_list.append(new_row)
                new_row = []
                end = time.time()
                row_time = end - start
                start = time.time()

                if((i + 1) % 1000000 == 0):
                    print('Done reading {} % of file - time/row = {}'.format(i/len(all_lines) * 100, row_time))

        return np.array(output_list)




test_file = '/media/tylerviducic/Elements/aidapt/data/recon/twopi_ppip.10.zzz'
test_manager = DataManager(test_file)

start = time.time()
my_array = test_manager.get_numpy_array()
end = time.time()
print(my_array)
print('Array length: {}'.format(len(my_array)))
print("time was " + str(end - start))

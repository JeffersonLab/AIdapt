# by Tyler Viducic and Torri Jeski

import numpy as np
from event import Event
from fiducialCuts import FiducialCuts
import time
import matplotlib.pyplot as plt
from dataManager import DataManager
import math

# Read in data here 


start = time.time()

# data_file = '/media/tylerviducic/Elements/aidapt/data/synthetic/clasfilter2_5M780.npy' # change to your path, obviously
data_file = '/media/tylerviducic/Elements/aidapt/data/recon/twopi_ppip.10.zzz'

data_manager = DataManager(data_file)

input_array = data_manager.get_numpy_array()

output_list = []
phi_list = []
num_bins = 180

num_rows, num_columns = input_array.shape

for n in range(num_rows):

    row = input_array[n]
    event = Event(row)
    phi = math.degrees(abs(event.get_proton_phi()))
    phi_list.append(phi)

    fd = FiducialCuts(event)

    if fd.check_event_pass():
        output_list.append(row.tolist())

output_array = np.array(output_list)

end = time.time()

print('Size of output array: ' + str(output_array.shape[0]))
print('time/event = ' + str((end - start)/len(input_array)) + " seconds")

plt.hist(np.array(phi_list), num_bins)
plt.title("Phi distribution")
plt.show()


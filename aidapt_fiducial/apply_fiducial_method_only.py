import math
import numpy as np

def apply_fiducial_cuts(px, py, pz, proton=False):
    momentum = math.sqrt(px*px + py*py + pz*pz)
    theta = math.atan2(math.sqrt(px*px + py*py), pz)
    phi = abs(math.degrees(math.atan2(py, px)))

    phi_cuts = [ (0, 26), (34, 86), (94, 146), (154, 176) ]
    momentum_cut = 0.375 # in GeV
    costheta_cut = 0.985

    if proton==True and not momentum > momentum_cut:
        return False
    
    if math.cos(theta) > costheta_cut:
        return False
    
    for cut in phi_cuts:
        if cut[0] < phi < cut[1]:
            return True

    return False


data_file = '/media/tylerviducic/Elements/aidapt/data/synthetic/clasfilter2_5M780.npy'
data_array = np.load(data_file)

print("starting loop")

for event in data_array:
    proton = (event[2], event[5], event[8])
    pi_plus = (event[3], event[6], event[9])
    pi_minus = (event[4], event[7], event[10])

    if not apply_fiducial_cuts(proton[0], proton[1], proton[2], proton=True):
        print("Failed fiducial cut")
        print('*' * 50)
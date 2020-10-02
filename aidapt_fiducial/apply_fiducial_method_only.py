import math
import numpy as np

def apply_fiducial_cuts(px, py, pz, pid):
    
# define kinematics and cuts

    momentum = math.sqrt(px*px + py*py + pz*pz)
    theta = math.degrees(math.atan2(math.sqrt(px*px + py*py), pz))
    phi = math.degrees(math.atan2(py, px))
    sector = 0

    phi_cuts = [ (0, 26), (34, 86), (94, 146), (154, 176) ]
    momentum_cut_proton = 0.32 # in GeV
    theta_cut_proton = 10
    momentum_cut_pi = 0.125 # in GeV
    theta_cut_min_pi = 10
    theta_cut_max_pi = 120

    if abs(phi) < 30:
        sector = 1
    elif phi > 0:
        if phi <= 90:
            sector = 2
        elif phi <= 150:
            sector = 3
    if abs(phi) > 150:
        sector = 4
    elif phi < 0: 
        if phi >=-90:
            sector = 6
        elif phi >=-150:
            sector = 5


# apply cuts
# cuts can be found in "Analysis of pi+pi- production from the g11 Data Set"
# by M. Battaglieri, R. De Vita, L. Bibrzycki, L. Lesniak, and A Szczepaniak

    if pid == 2212:
        if momentum < 0.45 and theta < 35: 
            return False
        if momentum < momentum_cut_proton or theta < theta_cut_proton:
            print
            return False
        if momentum < 0.45 and math.cos(theta) >  0.819:
            return False
        for cut in phi_cuts:
            if cut[0] < abs(phi) < cut [1]:
                return True
        return False
    
    elif pid == 211:
        if sector == 1 and theta > 90:
            return False
        if sector == 3 and theta > 70:
            return False
        if sector == 5 and theta > 80:
            return False
        
        if momentum < momentum_cut_pi or theta < theta_cut_min_pi or theta > theta_cut_max_pi:
            return False
        for cut in phi_cuts:
            if cut[0] < abs(phi) < cut [1]:
                return True
        return False
    
    elif pid == -211:
        if sector == 1 and theta > 100:
            return False
        if (sector == 3 or sector == 5) and theta > 90:
            return False
        if sector == 6 and theta > 110:
            return False

        if momentum < momentum_cut_pi or theta < theta_cut_min_pi or theta > theta_cut_max_pi:
            print('momentum: {} - Theta: {}'.format(momentum, theta))
            return False
        for cut in phi_cuts:
            if cut[0] < abs(phi) < cut [1]:
                return True
        return False



data_file = '/media/tylerviducic/Elements/aidapt/data/synthetic/clasfilter2_5M780.npy'
data_array = np.load(data_file)
n_cut = 0

print("starting loop")

for event in data_array:
    proton = (event[2], event[5], event[8])
    pi_plus = (event[3], event[6], event[9])
    pi_minus = (event[4], event[7], event[10])

    # if not apply_fiducial_cuts(pi_plus[0], pi_plus[1], pi_plus[2], 211):
    #     n_cut += 1
    #     continue
    if not apply_fiducial_cuts(pi_minus[0], pi_minus[1], pi_minus[2], -211):
        n_cut += 1
        
    # if not apply_fiducial_cuts(proton[0], proton[1], proton[2], 2212):
    #     n_cut += 1 


print("fraction that failed fiducial cut: {}".format(n_cut/len(data_array) * 100))
# module for checking if event passes fiducial cut

import math

class FiducialCuts:

    def __init__(self, event, missing_pi_minus=True):
        self.missing_pi_minus = missing_pi_minus
        self.event = event
        self.phi_cut = 26.0 # in Degrees
        self.theta_cut = 0.985
        self.momentum_cut = 0.375 

    def check_event_pass(self):
        return self._check_if_event_pass_momentum() and self._check_if_event_pass_phi() and self._check_if_event_pass_theta()

    # Private methods

    def _passes_phi(self, phi):
        return math.degrees(phi) < abs(self.phi_cut)

    def _passes_theta(self, theta):
        return math.cos(theta) < self.theta_cut

    def _passes_momentum(self, momentum):
        return momentum > self.momentum_cut

    def _check_if_event_pass_phi(self):
        if self.missing_pi_minus:
            return self._passes_phi(self.event.get_proton_phi()) and self._passes_phi(self.event.get_pi_plus_phi())
        else: 
             return self._passes_phi(self.event.get_proton_phi()) and self._passes_phi(self.event.get_pi_plus_phi()) and self._passes_phi(self.event.get_pi_minus_phi())

    def _check_if_event_pass_theta(self):
        if self.missing_pi_minus:
            return self._passes_theta(self.event.get_proton_theta()) and self._passes_theta(self.event.get_pi_plus_theta())
        else: 
             return self._passes_theta(self.event.get_proton_theta()) and self._passes_theta(self.event.get_pi_plus_theta()) and self._passes_theta(self.event.get_pi_minus_theta())

    def _check_if_event_pass_momentum(self):
        return self._passes_momentum(self.event.get_proton_momentum())





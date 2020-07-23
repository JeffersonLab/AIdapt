# used to get information from synthetic datafile
import math

class Event:

    def __init__(self, event_array):
        self.proton = (event_array[2], event_array[5], event_array[8], event_array[11])
        self.pi_plus = (event_array[3], event_array[6], event_array[9], event_array[12])
        self.pi_minus = (event_array[4], event_array[7], event_array[10], event_array[13])        

    def get_proton_phi(self):
        return self._get_theta(self.proton)

    def get_pi_plus_phi(self):
        return self._get_phi(self.pi_plus)

    def get_pi_minus_phi(self):
        return self._get_phi(self.pi_minus)

    def get_proton_theta(self):
        return self._get_theta(self.proton)

    def get_pi_plus_theta(self):
        return self._get_theta(self.pi_plus)

    def get_pi_minus_theta(self):
        return self._get_theta(self.pi_minus)

    def get_proton_momentum(self):
        return self._get_momentum(self.proton)

    def get_pi_plus_momentum(self):
        return self._get_momentum(self.pi_plus)

    def get_pi_minus_momentum(self):
        return self._get_momentum(self.pi_minus)

    # Private methods

    def _get_phi(self, particle):
        return math.atan(particle[1] / particle[0])

    def _get_theta(self, particle):
        return math.atan(math.sqrt((particle[0] * particle[0]) + particle[1] * particle[1]) / particle[2])

    def _get_momentum(self, particle):
        return math.sqrt(particle[0] * particle[0] + particle[1] * particle[1] + particle[2] * particle[2])
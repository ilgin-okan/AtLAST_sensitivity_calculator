from atlast_sc.utils import Decorators
import astropy.units as u
from atlast_sc.utils import DataHelper

class InstrumentSpecificParameters:
    def __init__(self, instrument_name):
        self.instrument_name = instrument_name

    class Finer:
        def __init__(self, obs_freq):
            self._T_rx = self._set_receiver_temp(self, obs_freq)

        @property
        def T_rx(self):
            "Get the receiver temperature of FINER instrument"
            return self._T_rx

        @staticmethod
        def _set_receiver_temp(self, obs_freq):
            obs_freq = obs_freq.value # needed to compare double vals
            if obs_freq > 120.0 and obs_freq < 210.0:
                return 45.0 * u.K
            elif obs_freq > 210.0 and obs_freq < 360.0:
                return 75.0 * u.K
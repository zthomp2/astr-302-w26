#!/usr/bin/env python

class Dusty:
    def __init__(self):
        pass

class External_Radiation(Dusty):
    def __init__(self):
        pass

    class Combination_BB(External_Radiation):
        def __init__(self, spectrum=1, number_of_bb=None):
            self.spectrum = spectrum
            self.number_of_bb = number_of_bb
            self.temperatures = []
            self.luminosities = []
    
        def AddTemps(self, temps):
            for temp in temps:
                self.temperature.append(temp)
    
        def AddLuminosity(self, lums):
            for lum in lums:
                self.luminosites.append(lum)    
    
    class Broken_PL(External_Radiation):
        def __init__(self, spectrum=2, pl_n=None,):
            self.spectrum = spectrum
            self.pl_n = pl_n
            self.pl_lambda = []
            self.pl_k = []
    
        def AddTemps(self, _lambdas):
            for _lambda in _lambdas:
                self.pl_lambda.append(_lambda)
    
        def AddLuminosity(self, _ks):
            for _k in _ks:
                self.pl_k.append(_k)    
    
    class BB_Engelke_Marengo(External_Radiation):
        def __init__(self, spectrum=3, tbb=None, sio_fd=None):
            self.spectrum = spectrum
            self.tbb = tbb
            self.sio_fd = sio_fd
    
    class Files(External_Radiation):
        def __init__(self, spectrum=None, file=None):
            self.spectrum = spectrum
            self.file = file

#class Dust_Properties(Dusty):

#class Density_Distribution(Dusty):

#class Optical_Depth(Dusty):
    
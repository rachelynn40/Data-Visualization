"""Simple example:
    -Read in SPE file
    -Store in dataframe
    -Plot Spectrum
    -Export to html file and display on local host
"""


import becquerel as bq
import numpy as np
import matplotlib.pyplot as plt
import mpld3

spec1 = bq.Spectrum.from_file('../tests/samples/1110C NAA cave pottery.Spe')
spec2 = bq.Spectrum.from_file('../tests/samples/Mendocino_07-10-13_Acq-10-10-13.Spe')

spec1.plot()
mpld3.show()


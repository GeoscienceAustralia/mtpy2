# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:19:35 2017

@author: u64125
Fei.zhang@ga.gov.au
"""

from mtpy.core.mt import MT
import mtpy.analysis.geometry as mtg
import numpy as np


def test_fun():
    """
    test function
    :return: T/F
    """

    #mtObj = MT(r'C:\Git\mtpy\examples\data\edi_files\pb42c.edi')
    mtObj = MT(r'E:/Githubz/mtpy/examples/data/edi_files/pb42c.edi')

    eccentricity_pb42c = (np.array([ 0.01675639,  0.01038589,  0.00527011,  0.00638819,  0.01483804,
            0.00385233,  0.00513294,  0.00403781,  0.02862114,  0.02689821,
            0.01425044,  0.05686524,  0.05742524,  0.02696736,  0.0275285 ,
            0.03647819,  0.04721932,  0.06336521,  0.12789841,  0.16409303,
            0.20630821,  0.34261225,  0.3967886 ,  0.51629705,  0.56645987,
            0.52558696,  0.46954261,  0.48028767,  0.47490701,  0.44927612,
            0.45185046,  0.44143159,  0.43570377,  0.41537978,  0.40546014,
            0.38785478,  0.37174031,  0.34534557,  0.35510941,  0.32282644,
            0.28501461,  0.22463964,  0.20683855]),
            np.array([ 0.17132216,  0.2757994 ,  0.71263216,  0.50481657,  0.21604906,
            0.98931454,  0.75816349,  1.06885049,  0.23412284,  0.25015825,
            0.4117732 ,  0.06824775,  0.13024193,  0.49471091,  0.61126932,
            0.5471021 ,  0.6073574 ,  0.50578334,  0.30809787,  0.44938001,
            0.35430928,  0.20402482,  0.36750578,  0.30360427,  0.27660847,
            0.55139247,  0.53103062,  0.48771581,  0.19105325,  0.68542871,
            0.66189643,  0.1495947 ,  0.11353391,  0.09190586,  0.09006473,
            0.1079376 ,  0.13673274,  0.19349474,  0.23780856,  0.35159944,
            0.55386034,  0.78687532,  0.9654131 ]))

    eccentricity = mtg.eccentricity(z_object = mtObj.Z)
    #print eccentricity

    for i in range(2):
        differ = np.abs(eccentricity[i] - eccentricity_pb42c[i]) < 1e-8
        print differ
        assert np.all(differ)  # true if-only every element is true


if __name__ == "__main__":
    test_fun()

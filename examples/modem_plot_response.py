#!/bin/env python
# -*- coding: utf-8 -*-
"""
Description:
    plot the responses curves from ModEM output data.
    
References: 
    https://gajira.atlassian.net/browse/ALAMP-77

CreationDate:   22/09/2017
Developer:      fei.zhang@ga.gov.au

Revision History:
    LastUpdate:     22/09/2017   FZ
    LastUpdate:     dd/mm/yyyy  Who     Optional description
"""

# import section
import os

from mtpy.imaging.plot_response import PlotResponse


def plot_response():
    #### Default Inputs ####
    modem_data_dir = r'E:\Githubz\ModEM_plotResponse_Issue\ModEM_files'
    filestem = 'Modular_MPI_NLCG_100'
    datafn = 'ModEM_Data.dat'
    station_list = ['GB%02i' % n for n in xrange(1, 40)]  # ['GB01', 'GB02',....,'GB39']
    plot_z = False

    respfn = filestem + '.dat'

    for station in station_list[0:5]:

        # plot responses at a station

        resp_range = None
        # resp_range = (0.01, 10000)  # This limit should be big enough, otherwise the plot curve will be out.
        if resp_range is None:
            outfile = r'E:/tmp/test_plot_resp/plot_responses_NO_yrange.jpg'
        else:
            outfile = r'E:/tmp/test_plot_resp/plot_responses_with_yrange.jpg'

        robj = PlotResponse(data_fn=os.path.join(modem_data_dir, datafn),
                            # resp_fn=os.path.join(modem_data_dir, respfn),  #filestem+'.dat'),
                            plot_type=[station],
                            plot_z=plot_z,
                            #  ctmm='r',ctem='b',
                            res_limits=resp_range
                            )

        # save to different image formats to compare their quality. JPG appears best
        robj.plot(save2file=outfile)
        # robj.plot(save2file = outfile)
        # robj.plot(save2file = outfile)
        # robj.plot(save2file = outfile)
        # robj.plot(save2file = outfile) # will create a big html file


def main():
    """
    define my main function
    :return:
    """
    print("Template main()")

    return


# =============================================
# Section for quick test of this script
# ---------------------------------------------
if __name__ == "__main__":
    # call functions
    # main()

    plot_response()

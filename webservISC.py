'''
This code automatically download seismic phase information from International
Seismological Centersel and write it down into a text file.
There are about 70 million lines of data in this data base.

By: S. Mostafa Mousavi
mmousavi@stanford.edu
'''

import requests
import csv

st_yr = 1900  # start year
ed_yr = 2016  # end year
st_mn = 1    # start month
ed_mn = 13    # end month


serviceurl = 'http://www.isc.ac.uk/cgi-bin/web-db-v4?'
with open("ISC.txt", "w") as text_file:
    for yr in range (st_yr,ed_yr,1):
        print(yr)
        should_restart = True
        while should_restart:
            should_restart = False
            for mn in range (st_mn,ed_mn,1):
                url = serviceurl + 'out_format=CSV&request=STNARRIVALS&stnsearch=GLOBAL&' +\
                'tdef=on&phaselist=P,Pg,Pn,S,Sg,Sn,Lg,Rg,LQ,LR&searchshape=GLOBAL&' +\
                'start_year='+str(yr)+'&start_month='+str(mn)+'&start_day=01&start_time=00:00:00&' +\
                'end_year='+str(yr)+'&end_month='+str(mn+1)+'&end_day=01&end_time=00:00:00&' +\
                'min_mag=0.1&req_mag_agcy=Any&req_mag_type=Any'

                r = requests.get(url)
                txt = r.text

                for line in txt:
                    print(line)
                    if line.find('Sorry') == 0:
                        print(line)
                        should_restart = True
                        break
                    elif line.find(str(yr)) > 80 and line.find(str(yr)) < 90:
                        # print(line.find(str(yr)))
                        # print(line)
                        text_file.write(line + "\n")
text_file.close()



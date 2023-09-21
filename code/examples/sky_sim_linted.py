#! /usr/bin/env python
"""
Simulate a catalog of stars near to the Andromeda constellation
"""

import math
import random

NSRC = 1_000_000


def get_radec():
    # from wikipedia
    andromeda_ra = '00:42:44.3'
    andromeda_dec = '41:16:09'

    degrees, minutes, seconds = andromeda_dec.split(':')
    dec = int(degrees)+int(minutes)/60+float(seconds)/3600

    hours, minutes, seconds = andromeda_ra.split(':')
    ra = 15*(int(hours)+int(minutes)/60+float(seconds)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    return ra, dec


def make_stars(ra, dec, nsrc=NSRC):
    ras = []
    decs = []
    for _ in range(nsrc):
        ras.append(ra + random.uniform(-1, 1))
        decs.append(dec + random.uniform(-1, 1))
    return ras, decs


if __name__ == "__main__":
    central_ra, central_dec = get_radec()
    ras, decs = make_stars(central_ra, central_dec)
    # now write these to a csv file for use by my other program
    with open('catalogue.csv', 'w', encoding='utf8') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print("Wrote catalogue.csv")

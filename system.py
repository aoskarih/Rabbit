#!/usr/bin/python3

import math

sun_mass = 1.989e30
G = 6.67428e-11
mu_sun = sun_mass * G

def switch (p1, p2):
    return p2, p1

def hohmann(r1, r2, Planet_mass):
    if r1 > r2:
        r1, r2 = switch(r1, r2)

    mu = Planet_mass * G
    delta_v1 = math.sqrt(mu / r1) * (math.sqrt((2 * r2) / (r1 + r2)) - 1)
    delta_v2 = math.sqrt(mu / r2) * (1 - math.sqrt((2 * r1) / (r1 + r2)))
    return delta_v1 + delta_v2

def interplanetary(planet_r1, planet_r2, Planet_mass_1, Planet_mass_2, orb_r1, orb_r2, mu_star):
    mu1 = Planet_mass_1 * G
    mu2 = Planet_mass_2 * G
    if planet_r1 > planet_r2:
        planet_r1, planet_r2 = switch(planet_r1, planet_r2)
        mu1, mu2 = switch(mu1, mu2)
        orb_r1, orb_r2 = switch(orb_r1, orb_r2)

    delta_v_hoh1 = math.sqrt(mu_star / planet_r1) * (math.sqrt((2 * planet_r2) / (planet_r1 + planet_r2)) - 1)
    delta_v1 = math.sqrt(delta_v_hoh1**2 + 2 * (mu1/orb_r1)) - math.sqrt(mu1/orb_r1)

    delta_v_hoh2 = math.sqrt(mu_star / planet_r2) * (1 - math.sqrt((2 * planet_r1) / (planet_r1 + planet_r2)))
    delta_v2 = math.sqrt(delta_v_hoh2**2 + 2 * (mu2/orb_r2)) - math.sqrt(mu2/orb_r2)
    return delta_v1 + delta_v2

def stellar_departure(r, velocity, mu_star):
    return math.sqrt(velocity**2 + 2*(mu_star/r)) - math.sqrt(mu_star/r)

def Orbital_period(periapsis, apoapsis, mu_centre):
    return 2*math.pi*math.sqrt(((periapsis + apoapsis)/2)/mu_centre)

def stellar_TOF (distance, velocity):
    return distance/velocity




print(stellar_departure(15e8, 3000000, mu_sun), ' DV of departure')
print(stellar_TOF(8e16, 3000000)/(3600*24*365), ' years')
print(stellar_departure(15e10, 3000000, mu_sun*2), ' DV of arrival')

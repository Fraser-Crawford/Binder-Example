import numpy as np

molar_mass_air = 28.9647e-3
molar_mass_water = 18.02e-3

def saturation_vapour_pressure(temperature:float)->float:
    return 0.61078e3 * np.exp(17.27*(temperature-273.15)/(temperature+237.3-273.15))


def vapour_mass_fraction_from_vapour_pressure(vapour_pressure:float, pressure:float=101325.0)->float:
    return molar_mass_water * vapour_pressure / (molar_mass_water * vapour_pressure + molar_mass_air * (pressure - vapour_pressure))


def wet_bulb_temperature(temperature:float,rh:float)->float:
    T=temperature-273.15
    rh_percent = rh*100
    return 273.15+(T * np.atan(0.151977*np.sqrt(rh_percent+8.313659))
            + 0.00391838*np.sqrt(rh_percent**3)*np.atan(0.023101*rh_percent)
            -np.atan(rh_percent-1.676331)
            +np.atan(T+rh_percent)
            -4.68035)

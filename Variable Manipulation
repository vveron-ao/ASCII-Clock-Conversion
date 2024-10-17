import math
print()

#Calculating Reynolds Law: Re = (u * l) / v
u = 9   #Fluid of Velocity: 9 m/s 
l = 0.875  #Characteristic Linear Dimension: 0.875 m
v = 0.0015  #Kinematic Viscosity: 0.0015 m^2/s
Re = ((u * l) / v)
print("Reynolds number is", Re)


#Calculating Bragg's Law: ny = 2d(Sin(Theta))
theta =  ((7 * math.pi) / 36)   #Scattering angle of 35 degrees.
d = 0.028   #Distance in nm (nanometers)
wavelength = (2 * d) * (math.sin(theta))  #The calculation for wavelength with formula.
print("Wavelength is", wavelength, "nm")


#Calculating Arps Equation: q(t) = (qi) / (1 + (b * Di * t) ^ (1 / b)
t = 10    #Production rate after 10 days
qi = 100  #initial production rate of barrels/day
Di = 2    #initial decline rate of barrels/day
b = 0.8   #hyperbolic constant
qt = (qi) / ((1 + b * Di * t) ** (1 / b))
print("Production rate is", qt , "barrels/day")


#Calculating Tsiolkovsky Rocket Equation: DeltaV = ve * ln(m0 / mf)
ve = 2028   #exhaust velocity of 2028 m/s
m0 = 11000  #initial mass of 11000 kg
mf = 8300   #final mass of 8300 kg
DeltaV = ((ve) * (math.log(m0 / mf)))
print("Change of velocity is", DeltaV, "m/s")

import math
import random
import time

# International system of units (let's not recreate the time NASA got the metric system confused and caused the destruction of a multimillion dollar probe)
# Also using real world data
FUSELAGE_WEIGHT = 10000
FUEL = 100000
THRUST = 1500000 # Newtons
USAGE_RATE = 500 # kg/s
CROSS_SECTIONAL = 10  # m^2 (frontal area)

AIR_DENSITY = 1.225
DRAG_COEFICIENT = 0.3  # Drag coefficient (simplified)
SCALE_HEIGHT = 8500 # exponential decrease as atmosphere gets thinner at higher altitudes
GRAVITY = 9.81

sim_time = 0
sim_speed = 1 # x1 speed

def ResetSimulation(speed):
    global sim_time
    global sim_speed

    sim_time = 0
    sim_speed = speed


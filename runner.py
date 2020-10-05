from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random



from population import Population 


# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa


def generate_routefile():
    random.seed(42)  # make tests reproducible
    N = 3600  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    with open("sumo_simulation/smartcities.rou.xml", "w") as routes:
        print("""<routes>
    <vType id="slow_car" accel="1" decel="6" length="6" minGap="0.2" maxSpeed="30.0" sigma="0.0" color="0,1,0"/>
    <vType id="medium_car" accel="2" decel="8" length="5" minGap="0.2" maxSpeed="40.0" sigma="0.0" color="0,1,1"/>
    <vType id="fast_car" accel="3" decel="9" length="3" minGap="0.2" maxSpeed="60.0" sigma="0.0" color="1,0,0"/>
 
    <vType id="fast_bus" accel="3" decel="6" length="10" minGap="0.2" maxSpeed="30.0" sigma="0.0" color="1,0,0" guiShape="bus"/>
    <vType id="slow_bus" accel="1" decel="8" length="10" minGap="0.2" maxSpeed="20.0" sigma="0.0" color="0,1,0" guiShape="bus"/>

    <vType id="slow_motorcycle" accel="2" decel="5" length="3" minGap="0.2" maxSpeed="30.0" sigma="0.0" color="255,255,255" guiShape="motorcycle"/>
    <vType id="fast_motorcycle" accel="3" decel="4" length="3" minGap="0.2" maxSpeed="60.0" sigma="0.0" color="1,0,0" guiShape="motorcycle"/>

    <route id="AL_A/A_B/B_C/C_CR" edges="AL_A A_B B_C C_CR"/>
    <route id="CR_C/C_B/B_A/A_AL" edges="CR_C C_B B_A A_AL"/>
    <route id="DR_D/D_E/E_F/F_FL" edges="DR_D D_E E_F F_FL"/>
    <route id="FL_F/F_E/E_D/D_DR" edges="FL_F F_E E_D D_DR"/>
        """, file=routes)
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="right_%i" type="slow_car" route="AL_A/A_B/B_C/C_CR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="left_%i" type="slow_car" route="AL_A/A_B/B_C/C_CR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="down_%i" type="slow_car" route="AL_A/A_B/B_C/C_CR" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
        print("</routes>", file=routes)

# The program looks like this
#    <tlLogic id="0" type="static" programID="0" offset="0">
# the locations of the tls are      NESW
#        <phase duration="31" state="GrGr"/>
#        <phase duration="6"  state="yryr"/>
#        <phase duration="31" state="rGrG"/>
#        <phase duration="6"  state="ryry"/>
#    </tlLogic>


def run():
    create_generation = Population()
    """execute the TraCI control loop"""
    step = 0
    # we start with phase 2 where EW has green
    print(create_generation.Principle())
    posicao = create_generation.Principle()
    posicao_final = posicao[0][2]
    traci.trafficlight.setPhaseDuration("A", posicao_final)
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        if traci.trafficlight.getPhase("A") == 2:
            # we are not already switching
            if traci.inductionloop.getLastStepVehicleNumber("A") > 0:
                # there is a vehicle from the north, switch
                traci.trafficlight.setPhase("A", 3)
            else:
                # otherwise try to keep green for EW
                traci.trafficlight.setPhase("A", 2)
        step += 1
    traci.close()
    sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    generate_routefile()

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "sumo_simulation/smartcities.sumo.cfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()

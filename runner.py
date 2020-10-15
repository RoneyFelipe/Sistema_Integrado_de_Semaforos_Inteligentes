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
    N = 720  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    # pSN = 1. / 31
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

   <route id="FB_F/F_A/A_AT" edges="FB_F F_A A_AT"/>
   <route id="AT_A/A_F/F_FB" edges="AT_A A_F F_FB"/>
   <route id="CT_C/C_D/D_DB" edges="CT_C C_D D_DB"/>
   <route id="DB_D/D_C/C_CT" edges="DB_D D_C C_CT"/>

   <route id="FB_F/F_E/E_EB" edges="FB_F F_E E_EB"/>
   <route id="FB_F/F_E/E_D/D_DB" edges="FB_F F_E E_D D_DB"/>
   <route id="EB_E/E_D/D_DB" edges="EB_E E_D D_DB"/>
   <route id="BT_B/B_A/A_AT" edges="BT_B B_A A_AT"/>
   <route id="BT_B/B_A/A_AL" edges="BT_B B_A A_AL"/>
   <route id="BT_B/B_C/C_CT" edges="BT_B B_C C_CT"/>
   <route id="BT_B/B_C/C_CR" edges="BT_B B_C C_CR"/>

     <route id="AT_A/A_F/F_FL" edges="AL_A A_F F_FL"/>
     <route id="AT_A/A_F/F_E/E_EB" edges="AT_A A_F F_E E_EB"/>
     <route id="AT_A/A_F/F_E/E_D/D_DB" edges="AT_A A_F F_E E_D D_DB"/>
     <route id="AT_A/A_F/F_E/E_D/D_DR" edges="AT_A A_F F_E E_D D_DB"/>
     <route id="AT_A/A_B/B_C/C_D/D_DB" edges="AL_A A_B B_C C_D D_DB"/>
     <route id="AT_A/A_B/B_C/C_D/D_DR" edges="AL_A A_B B_C C_D D_DR"/>


     <route id="CT_C/C_D/D_E/E_F/F_FL" edges="CT_C C_D D_E E_F F_FL"/>
     <route id="CT_C/C_D/D_E/E_F/F_FB" edges="CT_C C_D D_E E_F F_FB"/>
     <route id="CT_C/C_D/D_DR" edges="CT_C C_D D_DR"/>
     <route id="CT_C/C_B/B_BT" edges="CT_C C_B B_BT"/>
     <route id="CT_C/C_B/B_A/A_AL" edges="CT_C C_B B_A A_AL"/>
     <route id="CT_C/C_B/B_A/A_AT" edges="CT_C C_B B_A A_AT"/>



     <route id="FB_F/F_A/A_B/B_C/C_CR" edges="FB_F F_A A_B B_C C_CR"/>
     <route id="FB_F/F_A/A_B/B_C/C_D/D_DB" edges="FB_F F_A A_B B_C C_CR C_D D_DB"/>
     <route id="FB_F/F_A/A_B/B_C/C_D/D_DR" edges="FB_F F_A A_B B_C C_CR C_D D_DR"/>
     <route id="FB_F/F_E/E_D/D_C/C_CR" edges="FB_F F_E E_D D_C C_CR"/>
     <route id="FB_F/F_E/E_D/D_C/C_CT" edges="FB_F F_E E_D D_C C_CT"/>


     <route id="AL_A/A_B/B_C/C_D/D_DR" edges="AL_A A_B B_C C_D D_DB"/>
     <route id="AL_A/A_B/B_C/C_D/D_DB" edges="AL_A A_B B_C C_D D_DB"/>
     <route id="AL_A/A_F/F_FB" edges="AL_A A_F F_FB"/>
     <route id="AL_A/A_F/F_FL" edges="AL_A A_F F_FL"/>
     <route id="AL_A/A_F/F_E/E_EB" edges="AL_A A_F F_E E_EB"/>
     <route id="AL_A/A_F/F_E/E_D/D_DR" edges="AL_A A_F F_E E_D D_DR"/>
     <route id="AL_A/A_F/F_E/E_D/D_DB" edges="AL_A A_F F_E E_D D_DB"/>

     <route id="CR_C/C_CT" edges="CR_C C_CT"/>
     <route id="CR_C/C_B/B_BT" edges="CR_C C_B B_BT"/>
     <route id="CR_C/C_B/B_A/A_AT" edges="CR_C C_B B_A A_AT"/>

     <route id="DR_D/D_DB" edges="DR_D D_DB"/>
     <route id="DR_D/D_C/C_CR" edges="DR_D D_C C_CR"/>
     <route id="DR_D/D_C/C_CT" edges="DR_D D_C C_CT"/>
     <route id="DR_D/D_E/E_F/F_A/A_AT" edges="DR_D D_E E_F F_A A_AT"/>

     <route id="FL_F/F_E/E_EB" edges="FL_F F_E E_EB"/>
     <route id="FL_F/F_E/E_D/D_DB" edges="FL_F F_E E_D D_DB"/>
     <route id="FL_F/F_FB" edges="FL_F F_FB"/>
     <route id="FL_F/F_A/A_AT" edges="FL_F F_A A_AT"/>

        """, file=routes)
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="right_%i" type="slow_car" route="AL_A/A_B/B_C/C_CR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="right_%i" type="slow_car" route="CR_C/C_B/B_A/A_AL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="right_%i" type="slow_car" route="AT_A/A_F/F_FB" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="right_%i" type="slow_car" route="FB_F/F_A/A_AT" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="right_%i" type="slow_car" route="DB_D/D_C/C_CT" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="right_%i" type="slow_car" route="CT_C/C_D/D_DB" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="left_%i" type="slow_car" route="FL_F/F_E/E_D/D_DR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="down_%i" type="slow_car" route="DR_D/D_E/E_F/F_FL" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
        print("</routes>", file=routes)

def run():
    
    """execute the TraCI control loop"""
    create_generation = Population()
    step = 0
    position = create_generation.Principle()
    time_of_green = position[0][2]
    time_of_red = position[0][1]
    cycle = 0
    print('Tempo de Verde',time_of_green)
    print('Tempo de Vermelho',time_of_red)
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep() 
        if cycle == 0 and traci.trafficlight.getPhase("A") == 0: 
            traci.trafficlight.setPhase("A", 0)
            traci.trafficlight.setPhase("B", 0)
            traci.trafficlight.setPhase("C", 0)
            traci.trafficlight.setPhase("E", 0)
            traci.trafficlight.setPhase("F", 0)
            traci.trafficlight.setPhaseDuration("A",  time_of_green)
            traci.trafficlight.setPhaseDuration("B",  time_of_green)
            traci.trafficlight.setPhaseDuration("C",  time_of_green)
            traci.trafficlight.setPhaseDuration("E",  time_of_green)
            traci.trafficlight.setPhaseDuration("F",  time_of_green)
            cycle = 1
            #Adicionar o tempo de amarelo
        else:
            if cycle == 1 and traci.trafficlight.getPhase("A") == 2:
                traci.trafficlight.setPhase("A", 2)
                traci.trafficlight.setPhase("B", 2)
                traci.trafficlight.setPhase("C", 2)
                traci.trafficlight.setPhase("E", 2)
                traci.trafficlight.setPhase("F", 2)
                traci.trafficlight.setPhaseDuration("A",  time_of_red)
                traci.trafficlight.setPhaseDuration("B",  time_of_red)
                traci.trafficlight.setPhaseDuration("C",  time_of_red)
                traci.trafficlight.setPhaseDuration("E",  time_of_red)
                traci.trafficlight.setPhaseDuration("F",  time_of_red)
                cycle = 0
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

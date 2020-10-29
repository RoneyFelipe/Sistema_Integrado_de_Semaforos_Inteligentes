from __future__ import absolute_import #Importação das dependências necessárias
from __future__ import print_function #Importação das dependências necessárias

import os #Importação das dependências necessárias
import sys #Importação das dependências necessárias
import optparse #Importação das dependências necessárias
import random #Importação das dependências necessárias

from population import Population #Importação das dependências necessárias


# we need to import python modules from the $SUMO_HOME/tools directory

if 'SUMO_HOME' in os.environ: #Configurações para conexão com o SUMO
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools') #Configurações para conexão com o SUMO
    sys.path.append(tools) #Configurações para conexão com o SUMO
else:
    sys.exit("please declare environment variable 'SUMO_HOME'") #Configurações para conexão com o SUMO

from sumolib import checkBinary #Importação das dependências necessárias
import traci #Importação das dependências necessárias


def generate_routefile():
    random.seed(42)  # make tests reproducible
    N = 14400  #Tempo de execução da simulação
    #demanda por segundo de diferentes direções
    pWE_car = 1. / 30 #Demanda por segundo na direção Oeste-Leste para carros
    pEW_car = 1. / 31 #Demanda por segundo na direção Leste-Oeste para carros
    pNS_car = 1. / 50 #Demanda por segundo na direção Norte-Sul para carros
    pSN_car = 1. / 51 #Demanda por segundo na direção Sul-Norte para carros

    pWE_motorcycle = 1. / 80 #Demanda por segundo na direção Oeste-Leste para Motos
    pEW_motorcycle = 1. / 81 #Demanda por segundo na direção Leste-Oeste para Motos
    pNS_motorcycle = 1. / 90 #Demanda por segundo na direção Norte-Sul para Motos
    pSN_motorcycle = 1. / 91 #Demanda por segundo na direção Sul-Norte para Motos

    pWE_bus = 1. / 150 #Demanda por segundo na direção Oeste-Leste para ônibus
    pEW_bus = 1. / 151 #Demanda por segundo na direção Leste-Oeste para ônibus

    with open("sumo_simulation/smartcities.rou.xml", "w") as routes:
        print("""<routes>
    <vType id="slow_car" accel="1" decel="6" length="6" minGap="0.2" maxSpeed="30.0" sigma="0.0" color="0,1,0"/>
    <vType id="medium_car" accel="2" decel="8" length="5" minGap="0.2" maxSpeed="40.0" sigma="0.0" color="0,1,1"/>
    <vType id="fast_car" accel="3" decel="9" length="4" minGap="0.2" maxSpeed="60.0" sigma="0.0" color="1,0,0"/>
 
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
        #Estabelece os veículos que circularão na simulação
        for i in range(N):
            #Cars
            if random.uniform(0, 1) < pWE_car:
                print('    <vehicle id="right_%i" type="slow_car" route="AL_A/A_B/B_C/C_CR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW_car:
                print('    <vehicle id="left_%i" type="slow_car" route="CR_C/C_B/B_A/A_AL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW_car:
                print('    <vehicle id="left_%i" type="slow_car" route="DR_D/D_E/E_F/F_FL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pWE_car:
                print('    <vehicle id="rigth_%i" type="slow_car" route="FL_F/F_E/E_D/D_DR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS_car:
                print('    <vehicle id="north_%i" type="slow_car" route="AT_A/A_F/F_FB" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS_car:
                print('    <vehicle id="north_%i" type="slow_car" route="CT_C/C_D/D_DB" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pSN_car:
                print('    <vehicle id="south_%i" type="slow_car" route="FB_F/F_A/A_AT" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pSN_car:
                print('    <vehicle id="south_%i" type="slow_car" route="DB_D/D_C/C_CT" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pWE_car:
                print('    <vehicle id="right_%i" type="medium_car" route="AL_A/A_B/B_C/C_CR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW_car:
                print('    <vehicle id="left_%i" type="medium_car" route="CR_C/C_B/B_A/A_AL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW_car:
                print('    <vehicle id="left_%i" type="medium_car" route="DR_D/D_E/E_F/F_FL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pWE_car:
                print('    <vehicle id="rigth_%i" type="medium_car" route="FL_F/F_E/E_D/D_DR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS_car:
                print('    <vehicle id="north_%i" type="medium_car" route="AT_A/A_F/F_FB" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pNS_car:
                print('    <vehicle id="north_%i" type="medium_car" route="CT_C/C_D/D_DB" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pSN_car:
                print('    <vehicle id="south_%i" type="medium_car" route="FB_F/F_A/A_AT" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pSN_car:
                print('    <vehicle id="south_%i" type="medium_car" route="DB_D/D_C/C_CT" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pWE_car:
                print('    <vehicle id="right_%i" type="fast_car" route="AL_A/A_B/B_C/C_CR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW_car:
                print('    <vehicle id="left_%i" type="fast_car" route="CR_C/C_B/B_A/A_AL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            #Buses
            if random.uniform(0, 1) < pWE_bus:
                print('    <vehicle id="right_%i" type="slow_bus" route="AL_A/A_B/B_C/C_CR" depart="%i"> <stop busStop="busstop1" duration="25"/> </vehicle>' % (
                vehNr, i), file=routes)
            vehNr += 1

            if random.uniform(0, 1) < pEW_bus:
                print('    <vehicle id="left_%i" type="slow_bus" route="CR_C/C_B/B_A/A_AL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW_bus:
                print('    <vehicle id="left_%i" type="slow_bus" route="DR_D/D_E/E_F/F_FL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pWE_bus:
                print('    <vehicle id="rigth_%i" type="slow_bus" route="FL_F/F_E/E_D/D_DR" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            #Motorcycles
            if random.uniform(0, 1) < pWE_motorcycle:
                print('    <vehicle id="right_%i" type="slow_motorcycle" route="AL_A/A_F/F_FB" depart="%i" />' % (
                vehNr, i), file=routes)
            vehNr += 1

            if random.uniform(0, 1) < pEW_motorcycle:
                print('    <vehicle id="left_%i" type="slow_motorcycle" route="DR_D/D_C/C_CT" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pEW_motorcycle:
                print('    <vehicle id="left_%i" type="slow_motorcycle" route="BT_B/B_A/A_AL" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

            if random.uniform(0, 1) < pWE_motorcycle:
                print('    <vehicle id="rigth_%i" type="slow_motorcycle" route="EB_E/E_D/D_DB" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1

        print("</routes>", file=routes) #Insere as rotas no arquivo smartcities.rou.xml

def run():
    """execute the TraCI control loop"""
    create_generation = Population() #Atribui a classe population do arquivo population.py a variável create_generation
    step = 0 #Variável que controla o loop de execução da Traci para manipular a simulação
    position = create_generation.Principle() #Executa o metódo Principle reponsável por gerar os indivíduos que serão inseridos na simulação
    cycle_phase = 0 #Variável que controla o ciclo de cada fase, alterando se verde para vermelho quando necessário
    chosen_individual = 0 #Variável que seleciona o indivíduo, dentro da matriz, que será testada na simulação
    time_controller = 1 #Contrala o tempo de testagem de cada indivíduo

    print('|---Início da Simulação---|')
    print('|-------------------------|')

    while chosen_individual < 20:
        time_of_green = position[chosen_individual][2] #Seleciona o tempo de verde do indivíduo que será testado
        time_of_red = position[chosen_individual][1] #Seleciona o tempo de vermelho do indivíduo que será testado

        print('  Indivíduo selecionado:',chosen_individual)
        print('  Tempo de Verde:', time_of_green)
        print('  Tempo de Vermelho:', time_of_red)
        print('|--------------------------|')

        while traci.simulation.getTime() <= 720 * time_controller: #Loop responsável por controlar toda a simulação por meio da Traci
            traci.simulationStep() #Inicia a simulação
            if cycle_phase == 0 and traci.trafficlight.getPhase("A") == 0: #Confere se o semáforo está na phase 0 (Verde) e se ainda não receberam o tempo de verde total (cycle_phase=0)
                traci.trafficlight.setPhase("A", 0) #Insere a phase 0 no semáforo A. As phase foram declaradas no arquivo smartcities.tls.xml
                traci.trafficlight.setPhase("B", 0) #Insere a phase 0 no semáforo B. As phase foram declaradas no arquivo smartcities.tls.xml
                traci.trafficlight.setPhase("C", 0) #Insere a phase 0 no semáforo C. As phase foram declaradas no arquivo smartcities.tls.xml
                traci.trafficlight.setPhase("E", 0) #Insere a phase 0 no semáforo E. As phase foram declaradas no arquivo smartcities.tls.xml
                traci.trafficlight.setPhase("F", 0) #Insere a phase 0 no semáforo F. As phase foram declaradas no arquivo smartcities.tls.xml
                traci.trafficlight.setPhaseDuration("A",  time_of_green) #Adiciona o tempo de verde, fornecido pelo indivíduo que está sendo testado, ao semáforo A.
                traci.trafficlight.setPhaseDuration("B",  time_of_green) #Adiciona o tempo de verde, fornecido pelo indivíduo que está sendo testado, ao semáforo B.
                traci.trafficlight.setPhaseDuration("C",  time_of_green) #Adiciona o tempo de verde, fornecido pelo indivíduo que está sendo testado, ao semáforo C.
                traci.trafficlight.setPhaseDuration("E",  time_of_green) #Adiciona o tempo de verde, fornecido pelo indivíduo que está sendo testado, ao semáforo E.
                traci.trafficlight.setPhaseDuration("F",  time_of_green) #Adiciona o tempo de verde, fornecido pelo indivíduo que está sendo testado, ao semáforo F.
                cycle_phase = 1 #Significa que os semáforos receberam o tempo de verde, ou seja, quando a phase 0 e o tempo fixo de amarelo chegarem ao fim deve-se inserir o tempo de vermelho (cycle_phase=1)
                
            else:
                if cycle_phase == 1 and traci.trafficlight.getPhase("A") == 2: #Confere se o semáforo está na phase 1 (Vermelho) e se ainda não receberam o tempo de vermelho total (cycle_phase=1)
                    traci.trafficlight.setPhase("A", 2) #Insere a phase 2 no semáforo A. As phase foram declaradas no arquivo smartcities.tls.xml
                    traci.trafficlight.setPhase("B", 2) #Insere a phase 2 no semáforo B. As phase foram declaradas no arquivo smartcities.tls.xml
                    traci.trafficlight.setPhase("C", 2) #Insere a phase 2 no semáforo C. As phase foram declaradas no arquivo smartcities.tls.xml
                    traci.trafficlight.setPhase("E", 2) #Insere a phase 2 no semáforo E. As phase foram declaradas no arquivo smartcities.tls.xml
                    traci.trafficlight.setPhase("F", 2) #Insere a phase 2 no semáforo F. As phase foram declaradas no arquivo smartcities.tls.xml
                    traci.trafficlight.setPhaseDuration("A",  time_of_red) #Adiciona o tempo de vermelho, fornecido pelo indivíduo que está sendo testado, ao semáforo A.
                    traci.trafficlight.setPhaseDuration("B",  time_of_red) #Adiciona o tempo de vermelho, fornecido pelo indivíduo que está sendo testado, ao semáforo B.
                    traci.trafficlight.setPhaseDuration("C",  time_of_red) #Adiciona o tempo de vermelho, fornecido pelo indivíduo que está sendo testado, ao semáforo C.
                    traci.trafficlight.setPhaseDuration("E",  time_of_red) #Adiciona o tempo de vermelho, fornecido pelo indivíduo que está sendo testado, ao semáforo E.
                    traci.trafficlight.setPhaseDuration("F",  time_of_red) #Adiciona o tempo de vermelho, fornecido pelo indivíduo que está sendo testado, ao semáforo F.
                    cycle_phase = 0 #Significa que os semáforos receberam o tempo de vermelho, ou seja, quando a phase 2 chegar ao fim deve-se reiniciar o ciclo, voltando ao verde (cycle_phase=0)
            step += 1
            
        chosen_individual = chosen_individual + 1 #Seleciona a próxima posição do vetor que será testada
        time_controller = time_controller + 1 #Insere mais 720 segundos na simulação para que o próximo indivíduo seja testado
    print('|---Término da Simulação---|')
    traci.close() #Encerra a simulação
    sys.stdout.flush()

def get_options():
    optParser = optparse.OptionParser() #Configurações para conexão com o SUMO
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo") #Configurações para conexão com o SUMO
    options, args = optParser.parse_args() #Configurações para conexão com o SUMO
    return options

if __name__ == "__main__":
    options = get_options()
   
    if options.nogui: #Seleciona o SUMO ou SUMO-GUI para execução da simulação
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    generate_routefile() #Gera as rotas da simulação

    traci.start([sumoBinary, "-c", "sumo_simulation/smartcities.sumo.cfg",
                             "--tripinfo-output", "tripinfo.xml"]) #Executa a simulação utilizando a Traci via esse mesmo script python

    run()

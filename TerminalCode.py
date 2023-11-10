import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Fuzzy variables for voltage, torque, and speed are created. These variables define the universe of discourse for each variable.
voltage = ctrl.Antecedent(np.arange(0, 25, 1), 'voltage')
torque = ctrl.Antecedent(np.arange(0, 25, 1), 'torque')
speed = ctrl.Consequent(np.arange(0, 2500, 1), 'speed')

# 3 membership functions
# Membership functions are defined for each linguistic term of the variables using trimf method with is used to create the triangular membership curves

voltage['Very Low'] = fuzz.trimf(voltage.universe, [0, 5, 10])
voltage['Low'] = fuzz.trimf(voltage.universe, [4, 10, 15])
voltage['Medium'] = fuzz.trimf(voltage.universe, [8, 15, 20])
voltage['High'] = fuzz.trimf(voltage.universe, [12, 18, 25])
voltage['Very High'] = fuzz.trimf(voltage.universe, [18, 25, 25])

torque['Very Low'] = fuzz.trimf(torque.universe, [0, 5, 10])
torque['Low'] = fuzz.trimf(torque.universe, [4, 10, 15])
torque['Medium'] = fuzz.trimf(torque.universe, [8, 15, 20])
torque['High'] = fuzz.trimf(torque.universe, [12, 18, 25])
torque['Very High'] = fuzz.trimf(torque.universe, [18, 25, 25])

speed['Very Slow'] = fuzz.trimf(speed.universe, [0, 500, 1000])
speed['Slow'] = fuzz.trimf(speed.universe, [400, 1000, 1500])
speed['Moderate'] = fuzz.trimf(speed.universe, [800, 1500, 2000])
speed['Fast'] = fuzz.trimf(speed.universe, [1200, 2000, 2500])
speed['Very Fast'] = fuzz.trimf(speed.universe, [1800, 2500, 2500])

# Fuzzy rules are established to map combinations of input variables (voltage and torque) to the output variable (speed). Each rule is structured as an 'if-then' statement using the defined linguistic terms.
rule1 = ctrl.Rule(voltage['Very Low'] & torque['Very Low'], speed['Very Slow'])
rule2 = ctrl.Rule(voltage['Low'] & torque['Low'], speed['Slow'])
rule3 = ctrl.Rule(voltage['Medium'] & torque['Medium'], speed['Moderate'])
rule4 = ctrl.Rule(voltage['High'] & torque['High'], speed['Fast'])
rule5 = ctrl.Rule(voltage['Very High'] & torque['Very High'], speed['Very Fast'])

# A control system is created by combining all the defined rules. Then, a simulation object is generated using this control system.
system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
simulator = ctrl.ControlSystemSimulation(system)


# Input values for voltage and torque are set. The simulation is performed, and the output (Predicted Motor Speed) is computed based on the given input values following the defined fuzzy logic rules.
voltage_input = float(input("Enter the Voltage(V): "))
torque_input = float(input("Enter the Torque(Nm): "))

if voltage_input < 0 or voltage_input > 25 or torque_input < 0 or torque_input > 25:
    print("Input values should be between 0 and 25.")
else:
    simulator.input['voltage'] = voltage_input
    simulator.input['torque'] = torque_input
    try:
        simulator.compute()
        result = round(simulator.output['speed'], 2)
        print(f"Calculated Speed Output: {result}")

    except ValueError as e:
        print("Error: Crisp output cannot be calculated. Please check the input values and rules.")



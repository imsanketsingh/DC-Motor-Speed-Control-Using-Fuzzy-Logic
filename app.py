import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('legend', fontsize=6)

# Fuzzy logic setup
voltage = ctrl.Antecedent(np.arange(0, 25, 1), 'voltage')
torque = ctrl.Antecedent(np.arange(0, 25, 1), 'torque')
speed = ctrl.Consequent(np.arange(0, 1500, 1), 'speed')

# Membership functions
voltage['Very Low'] = fuzz.trimf(voltage.universe, [0, 5, 10])
voltage['Low'] = fuzz.trimf(voltage.universe, [4, 9, 14])
voltage['Medium'] = fuzz.trimf(voltage.universe, [8, 13, 18])
voltage['High'] = fuzz.trimf(voltage.universe, [12, 17, 22])
voltage['Very High'] = fuzz.trimf(voltage.universe, [16, 21, 25])

torque['Very Low'] = fuzz.trimf(torque.universe, [18, 25, 25])
torque['Low'] = fuzz.trimf(torque.universe, [12, 15, 20])
torque['Medium'] = fuzz.trimf(torque.universe, [8, 13, 16])
torque['High'] = fuzz.trimf(torque.universe, [4, 8, 12])
torque['Very High'] = fuzz.trimf(torque.universe, [0, 5, 8])

speed['Very Slow'] = fuzz.trimf(speed.universe, [0, 200, 400])
speed['Slow'] = fuzz.trimf(speed.universe, [200, 500, 600])
speed['Moderate'] = fuzz.trimf(speed.universe, [400, 600, 1000])
speed['Fast'] = fuzz.trimf(speed.universe, [700, 900, 1200])
speed['Very Fast'] = fuzz.trimf(speed.universe, [1000, 1300, 1500])


# Fuzzy rules
rule1 = ctrl.Rule(voltage['Very Low'] & torque['Very Low'], speed['Very Slow'])
rule2 = ctrl.Rule(voltage['Low'] & torque['Very Low'], speed['Very Slow'])
rule3 = ctrl.Rule(voltage['Medium'] & torque['Very Low'], speed['Very Slow'])
rule4 = ctrl.Rule(voltage['High'] & torque['Very Low'], speed['Slow'])
rule5 = ctrl.Rule(voltage['Very High'] & torque['Very Low'], speed['Slow'])

rule6 = ctrl.Rule(voltage['Very Low'] & torque['Low'], speed['Very Slow'])
rule7 = ctrl.Rule(voltage['Low'] & torque['Low'], speed['Slow'])
rule8 = ctrl.Rule(voltage['Medium'] & torque['Low'], speed['Slow'])
rule9 = ctrl.Rule(voltage['High'] & torque['Low'], speed['Moderate'])
rule10 = ctrl.Rule(voltage['Very High'] & torque['Low'], speed['Moderate'])

rule11 = ctrl.Rule(voltage['Very Low'] & torque['Medium'], speed['Slow'])
rule12 = ctrl.Rule(voltage['Low'] & torque['Medium'], speed['Moderate'])
rule13 = ctrl.Rule(voltage['Medium'] & torque['Medium'], speed['Moderate'])
rule14 = ctrl.Rule(voltage['High'] & torque['Medium'], speed['Fast'])
rule15 = ctrl.Rule(voltage['Very High'] & torque['Medium'], speed['Fast'])

rule16 = ctrl.Rule(voltage['Very Low'] & torque['High'], speed['Moderate'])
rule17 = ctrl.Rule(voltage['Low'] & torque['High'], speed['Fast'])
rule18 = ctrl.Rule(voltage['Medium'] & torque['High'], speed['Fast'])
rule19 = ctrl.Rule(voltage['High'] & torque['High'], speed['Very Fast'])
rule20 = ctrl.Rule(voltage['Very High'] & torque['High'], speed['Very Fast'])

rule21 = ctrl.Rule(voltage['Very Low'] & torque['Very High'], speed['Fast'])
rule22 = ctrl.Rule(voltage['Low'] & torque['Very High'], speed['Very Fast'])
rule23 = ctrl.Rule(voltage['Medium'] & torque['Very High'], speed['Very Fast'])
rule24 = ctrl.Rule(voltage['High'] & torque['Very High'], speed['Very Fast'])
rule25 = ctrl.Rule(voltage['Very High'] & torque['Very High'], speed['Very Fast'])


# control system, and simulator definitions
system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25])
simulator = ctrl.ControlSystemSimulation(system)


# Create a Streamlit app
st.set_page_config(page_title='DC Motor Speed Predictor', page_icon= 'images/favicon.png')
st.title('Fuzzy Logic Speed Control System')

# Input values (simulating user input)
voltage_input = st.slider('Voltage Input', min_value=0.0, max_value=25.0, value=15.0)
torque_input = st.slider('Torque Input', min_value=0.0, max_value=25.0, value=15.0)

if voltage_input < 0 or voltage_input > 25 or torque_input < 0 or torque_input > 25:
    st.warning("Input values should be between 0 and 25.")
else:
    simulator.input['voltage'] = voltage_input
    simulator.input['torque'] = torque_input
    try:
        simulator.compute()
        result = round(simulator.output['speed'], 2)
        st.markdown(f"Calculated DC Motor Speed Output: **{result}**")
        st.markdown("---")


        plot_width, plot_height = 6, 3

        # Generate the membership functions plot for voltage
        voltage_membership_fig, ax = plt.subplots(figsize=(plot_width, plot_height))
        ax.plot(voltage.universe, fuzz.trimf(voltage.universe, [0, 5, 10]), label='Very Low')
        ax.plot(voltage.universe, fuzz.trimf(voltage.universe, [4, 9, 14]), label='Low')
        ax.plot(voltage.universe, fuzz.trimf(voltage.universe, [8, 13, 18]), label='Medium')
        ax.plot(voltage.universe, fuzz.trimf(voltage.universe, [12, 17, 22]), label='High')
        ax.plot(voltage.universe, fuzz.trimf(voltage.universe, [16, 21, 25]), label='Very High')
        ax.fill_between(voltage.universe, fuzz.interp_membership(voltage.universe, fuzz.trimf(voltage.universe, [0, 5, 10]), voltage_input), alpha=0.2)
        ax.fill_between(voltage.universe, fuzz.interp_membership(voltage.universe, fuzz.trimf(voltage.universe, [4, 9, 14]),  voltage_input), alpha=0.2)
        ax.fill_between(voltage.universe, fuzz.interp_membership(voltage.universe, fuzz.trimf(voltage.universe, [8, 13, 18]), voltage_input), alpha=0.2)
        ax.fill_between(voltage.universe, fuzz.interp_membership(voltage.universe, fuzz.trimf(voltage.universe, [12, 17, 22]), voltage_input), alpha=0.2)
        ax.fill_between(voltage.universe, fuzz.interp_membership(voltage.universe, fuzz.trimf(voltage.universe, [16, 21, 25]), voltage_input), alpha=0.2)
        ax.legend()
        ax.set_xlabel('Voltage')
        ax.set_ylabel('Membership')
        st.write("Voltage Membership Function:")
        st.pyplot(voltage_membership_fig)

        # Generate the membership functions plot for torque
        torque_membership_fig, ax = plt.subplots(figsize=(plot_width, plot_height))
        ax.plot(torque.universe, fuzz.trimf(torque.universe, [18, 25, 25]), label='Very Low')
        ax.plot(torque.universe, fuzz.trimf(torque.universe, [12, 15, 20]), label='Low')
        ax.plot(torque.universe, fuzz.trimf(torque.universe, [8, 13, 16]), label='Medium')
        ax.plot(torque.universe, fuzz.trimf(torque.universe, [4, 8, 12]), label='High')
        ax.plot(torque.universe, fuzz.trimf(torque.universe, [0, 5, 8]), label='Very High')
        ax.fill_between(torque.universe, fuzz.interp_membership(torque.universe, fuzz.trimf(torque.universe, [18, 25, 25]), torque_input), alpha=0.2)
        ax.fill_between(torque.universe, fuzz.interp_membership(torque.universe, fuzz.trimf(torque.universe, [12, 15, 20]), torque_input), alpha=0.2)
        ax.fill_between(torque.universe, fuzz.interp_membership(torque.universe, fuzz.trimf(torque.universe, [8, 13, 16]), torque_input), alpha=0.2)
        ax.fill_between(torque.universe, fuzz.interp_membership(torque.universe, fuzz.trimf(torque.universe, [4, 8, 12]), torque_input), alpha=0.2)
        ax.fill_between(torque.universe, fuzz.interp_membership(torque.universe, fuzz.trimf(torque.universe, [0, 5, 8]), torque_input), alpha=0.2)
        ax.legend()
        ax.set_xlabel('Torque')
        ax.set_ylabel('Membership')
        st.write("Torque Membership Function:")
        st.pyplot(torque_membership_fig)

        st.markdown("*The changing colors in the membership function plots represent the degree of membership of the input value in each fuzzy set.*")
        st.markdown("---")

    

        # Generate the membership functions plot for speed
        speed_membership_fig, ax = plt.subplots(figsize=(plot_width, plot_height))
        ax.plot(speed.universe, fuzz.trimf(speed.universe, [0, 200, 400]), label='Very Slow')
        ax.plot(speed.universe, fuzz.trimf(speed.universe, [200, 500, 600]), label='Slow')
        ax.plot(speed.universe, fuzz.trimf(speed.universe, [400, 600, 1000]), label='Moderate')
        ax.plot(speed.universe, fuzz.trimf(speed.universe, [700, 900, 1200]), label='Fast')
        ax.plot(speed.universe, fuzz.trimf(speed.universe, [1000, 1300, 1500]), label='Very Fast')
        ax.fill_between(speed.universe, fuzz.interp_membership(speed.universe, fuzz.trimf(speed.universe, [0, 200, 400]), result), alpha=0.2)
        ax.fill_between(speed.universe, fuzz.interp_membership(speed.universe, fuzz.trimf(speed.universe, [200, 500, 600]), result), alpha=0.2)
        ax.fill_between(speed.universe, fuzz.interp_membership(speed.universe, fuzz.trimf(speed.universe, [400, 600, 1000]), result), alpha=0.2)
        ax.fill_between(speed.universe, fuzz.interp_membership(speed.universe, fuzz.trimf(speed.universe, [700, 900, 1200]), result), alpha=0.2)
        ax.fill_between(speed.universe, fuzz.interp_membership(speed.universe, fuzz.trimf(speed.universe, [1000, 1300, 1500]), result), alpha=0.2)
        ax.legend()
        ax.set_xlabel('Speed')
        ax.set_ylabel('Membership')
        st.write("Speed Membership Function:")
        st.pyplot(speed_membership_fig)

        st.markdown("*The colors in the speed membership function plot represent the degree of membership of the output value in each fuzzy set.*")
        st.markdown("*So, for example, if an output value has a high degree of membership in the 'Moderate' set, we see a larger colored area under the 'Moderate' curve.*")

    except ValueError as e:
        st.warning("Error: Crisp output cannot be calculated. Please check the input values and rules.")


st.markdown("---")

st.markdown(
    """
    <div style=" bottom: 10px; width: 100%; text-align: center;">
        <p style="color: #888;"> 
            <a href="https://github.com/imsanketsingh" style="color: #888;">Github</a> | 
            <a href="https://www.linkedin.com/in/imsanketsingh/" style="color: #888;">Linkedin</a> |
            <a href="https://github.com/imsanketsingh/DC-Motor-Speed-Control-Using-Fuzzy-Logic/" style="color: #888;">Code</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
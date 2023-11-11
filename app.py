import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st
import matplotlib.pyplot as plt

# Fuzzy logic setup
voltage = ctrl.Antecedent(np.arange(0, 25, 1), 'voltage')
torque = ctrl.Antecedent(np.arange(0, 25, 1), 'torque')
speed = ctrl.Consequent(np.arange(0, 2500, 1), 'speed')

# Membership functions with Gaussian functions
voltage['Very Low'] = fuzz.gaussmf(voltage.universe, 0, 3)
voltage['Low'] = fuzz.gaussmf(voltage.universe, 7, 3)
voltage['Medium'] = fuzz.gaussmf(voltage.universe, 13, 3)
voltage['High'] = fuzz.gaussmf(voltage.universe, 18, 3)
voltage['Very High'] = fuzz.gaussmf(voltage.universe, 25, 3)

torque['Very Low'] = fuzz.gaussmf(torque.universe, 0, 3)
torque['Low'] = fuzz.gaussmf(torque.universe, 7, 3)
torque['Medium'] = fuzz.gaussmf(torque.universe, 13, 3)
torque['High'] = fuzz.gaussmf(torque.universe, 18, 3)
torque['Very High'] = fuzz.gaussmf(torque.universe, 25, 3)

speed['Very Slow'] = fuzz.gaussmf(speed.universe, 0, 500)
speed['Slow'] = fuzz.gaussmf(speed.universe, 750, 500)
speed['Moderate'] = fuzz.gaussmf(speed.universe, 1250, 500)
speed['Fast'] = fuzz.gaussmf(speed.universe, 1750, 500)
speed['Very Fast'] = fuzz.gaussmf(speed.universe, 2500, 500)

# Fuzzy rules
rule1 = ctrl.Rule(voltage['Very Low'] & torque['Very Low'], speed['Very Slow'])
rule2 = ctrl.Rule(voltage['Low'] & torque['Low'], speed['Slow'])
rule3 = ctrl.Rule(voltage['Medium'] & torque['Medium'], speed['Moderate'])
rule4 = ctrl.Rule(voltage['High'] & torque['High'], speed['Fast'])
rule5 = ctrl.Rule(voltage['Very High'] & torque['Very High'], speed['Very Fast'])

# Create a Streamlit app
st.set_page_config(page_title='DC Motor Speed Predictor', page_icon= 'images/favicon.png')
st.title('Fuzzy Logic Speed Control System')

# Input values (simulating user input)
voltage_input = st.slider('Voltage Input', min_value=0.0, max_value=25.0, value=15.0)
torque_input = st.slider('Torque Input', min_value=0.0, max_value=25.0, value=15.0)

if voltage_input < 0 or voltage_input > 25 or torque_input < 0 or torque_input > 25:
    st.warning("Input values should be between 0 and 25.")
else:
    simulator = ctrl.ControlSystemSimulation(ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5]))
    simulator.input['voltage'] = voltage_input
    simulator.input['torque'] = torque_input
    try:
        simulator.compute()
        result = round(simulator.output['speed'], 2)
        st.markdown(f"Calculated DC Motor Speed Output: **{result}**")
        st.markdown("---")

        plot_width, plot_height = 6, 3

        # Generate the membership functions plot for voltage with Gaussian functions
        voltage_membership_fig, ax = plt.subplots(figsize=(plot_width, plot_height))
        ax.plot(voltage.universe, fuzz.gaussmf(voltage.universe, 0, 3), label='Very Low')
        ax.plot(voltage.universe, fuzz.gaussmf(voltage.universe, 7, 3), label='Low')
        ax.plot(voltage.universe, fuzz.gaussmf(voltage.universe, 13, 3), label='Medium')
        ax.plot(voltage.universe, fuzz.gaussmf(voltage.universe, 18, 3), label='High')
        ax.plot(voltage.universe, fuzz.gaussmf(voltage.universe, 25, 3), label='Very High')
        ax.legend()
        ax.set_xlabel('Voltage')
        ax.set_ylabel('Membership')
        st.write("Voltage Membership Function:")
        st.pyplot(voltage_membership_fig)

        # Generate the membership functions plot for torque with Gaussian functions
        torque_membership_fig, ax = plt.subplots(figsize=(plot_width, plot_height))
        ax.plot(torque.universe, fuzz.gaussmf(torque.universe, 0, 3), label='Very Low')
        ax.plot(torque.universe, fuzz.gaussmf(torque.universe, 7, 3), label='Low')
        ax.plot(torque.universe, fuzz.gaussmf(torque.universe, 13, 3), label='Medium')
        ax.plot(torque.universe, fuzz.gaussmf(torque.universe, 18, 3), label='High')
        ax.plot(torque.universe, fuzz.gaussmf(torque.universe, 25, 3), label='Very High')
        ax.legend()
        ax.set_xlabel('Torque')
        ax.set_ylabel('Membership')
        st.write("Torque Membership Function:")
        st.pyplot(torque_membership_fig)

        # Generate the membership functions plot for speed with Gaussian functions
        speed_membership_fig, ax = plt.subplots(figsize=(plot_width, plot_height))
        ax.plot(speed.universe, fuzz.gaussmf(speed.universe, 0, 500), label='Very Slow')
        ax.plot(speed.universe, fuzz.gaussmf(speed.universe, 750, 500), label='Slow')
        ax.plot(speed.universe, fuzz.gaussmf(speed.universe, 1250, 500), label='Moderate')
        ax.plot(speed.universe, fuzz.gaussmf(speed.universe, 1750, 500), label='Fast')
        ax.plot(speed.universe, fuzz.gaussmf(speed.universe, 2500, 500), label='Very Fast')
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

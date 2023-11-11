<!-- Project Title with Decorations -->
# Fuzzy Logic Speed Control System for DC Motors
**An interactive Python-based application for predictive speed control using Fuzzy Logic**

---

## Overview

The project presents a Fuzzy Logic-based system to predict and control DC motor speeds. Fuzzy logic enables handling imprecise input and rules, providing a robust method for controlling motor speeds.

### Features

- **Fuzzy Logic Setup**: Defines antecedents and consequents, membership functions for voltage, torque, and speed.
- **Membership Functions**:
  - Voltage: 'Very Low', 'Low', 'Medium', 'High', 'Very High'
  - Torque: 'Very Low', 'Low', 'Medium', 'High', 'Very High'
  - Speed: 'Very Slow', 'Slow', 'Moderate', 'Fast', 'Very Fast'
- **Fuzzy Rules**: Specifies relationships between input and output sets.
- **Visualization**: Membership function plots for voltage, torque, and speed to showcase the fuzzy sets and the degree of membership.
- **Streamlit App Integration**: Interactive interface to simulate user input and visualize the fuzzy system's outputs.

---

## Usage

To use the system:

1. **Installation**: Install the necessary libraries.
2. **Run the App**: Execute `streamlit run app.py`.
3. **Input Simulation**: Adjust the voltage and torque sliders to simulate different input scenarios.
4. **Output Visualization**: View the calculated speed output and membership function plots.

---

### Screenshots

Voltage Membership Function![image](https://github.com/imsanketsingh/DC-Motor-Speed-Control-Using-Fuzzy-Logic/assets/77242965/4d099b84-fd39-4fc9-9331-a1f5104e2d2e)

Torque Membership Function![image](https://github.com/imsanketsingh/DC-Motor-Speed-Control-Using-Fuzzy-Logic/assets/77242965/f991c1de-618c-4cc6-9ba0-cbde88303a19)

Speed Membership Function![image](https://github.com/imsanketsingh/DC-Motor-Speed-Control-Using-Fuzzy-Logic/assets/77242965/3b690d75-53ed-4a62-83e8-5559db694e8f)



---

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**: `git clone https://github.com/imsanketsingh/DC-Motor-Speed-Control-Using-Fuzzy-Logic.git`
2. **Install dependencies**: `pip install -r requirements.txt`

---

## Contributions

Contributions are welcome!

1. **Fork the repository**.
2. **Create a new branch** for your feature: `git checkout -b feature-name`
3. **Commit your changes**.
4. **Push to the branch** and **submit a pull request**.

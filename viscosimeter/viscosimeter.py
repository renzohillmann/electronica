"""
Main viscosimeter circuit script that creates a netlist for the viscosimeter schematic.
"""
# First, import the initialization script
import kicad_init

# Now import SKiDL and other modules
from skidl import *
import os

# Set up SKiDL to use KiCad libraries
set_default_tool(KICAD)

def create_viscosimeter_circuit():
    """Creates the viscosimeter circuit and generates a netlist"""
    
    # Define the power nets
    gnd = Net("GND")
    gnd.drive = POWER
    vcc12 = Net("+12V")
    vcc12.drive = POWER
    vcc5 = Net("+5V")
    vcc5.drive = POWER
    
    # Define signal nets
    voltage_monitor = Net("VOLTAGE_MONITOR")
    current_sense = Net("CURRENT_SENSE")
    proximity_out = Net("PROX_OUT")
    switch_out = Net("SW_OUT")
    motor_pos = Net("MOTOR_POS")
    
    # Create components from KiCad libraries
    
    # Resistors for voltage divider
    r1 = Part("Device", "R", value="48.7k", footprint="Resistor_SMD:R_0805_2012Metric")
    r2 = Part("Device", "R", value="31.4k", footprint="Resistor_SMD:R_0805_2012Metric")
    
    # Current sensor - using correct ACS712 part name
    acs712 = Part("Sensor_Current", "ACS712xLCTR-30A", 
                 footprint="Package_SO:SOIC-8_3.9x4.9mm_P1.27mm")
    
    # Motor - use a generic motor symbol
    motor = Part("Motor", "Motor_DC", 
                value="RS-445PA-14233R",
                footprint="TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal")
    
    # Proximity sensor TCD210245AA - using screw terminal (more compatible)
    prox_sensor = Part("Connector", "Screw_Terminal_01x03", 
                      value="TCD210245AA",
                      footprint="TerminalBlock:TerminalBlock_bornier-3_P5.08mm")
    
    # Switch - using a push button
    switch = Part("Switch", "SW_Push", 
                 footprint="Button_Switch_THT:SW_PUSH_6mm")
    
    # Arduino Uno - using a generic MCU with key pins defined
    arduino = Part("MCU_Module", "Arduino_UNO_R3", 
                  footprint="Module:Arduino_UNO_R3")
    
    # Power connectors
    pwr12v = Part("Connector", "Screw_Terminal_01x02", 
                 footprint="TerminalBlock:TerminalBlock_bornier-2_P5.08mm")
    
    # Create labels for power rails
    vcc12_label = Part("power", "PWR_FLAG")
    gnd_label = Part("power", "GND")
    vcc5_label = Part("power", "PWR_FLAG")
    
    # Connect power labels
    vcc12_label[1] += vcc12
    gnd_label[1] += gnd
    vcc5_label[1] += vcc5
    
    # Connect 12V supply terminals
    pwr12v[1] += vcc12
    pwr12v[2] += gnd
    
    # Connect voltage divider
    r1[1] += vcc12
    r1[2] += voltage_monitor
    r1[2] += r2[1]
    r2[2] += gnd
    
    # Connect current sensor
    acs712["VCC"] += vcc5
    acs712["GND"] += gnd
    acs712["VIOUT"] += current_sense
    acs712["IP+"] += vcc12
    acs712["IP-"] += motor_pos
    
    # Connect motor
    motor["+"] += motor_pos
    motor["-"] += gnd
    
    # Connect proximity sensor (3-pin connector: pin 1=VCC, pin 2=GND, pin 3=OUT)
    prox_sensor[1] += vcc5
    prox_sensor[2] += gnd
    prox_sensor[3] += proximity_out
    
    # Connect switch
    switch[1] += switch_out
    switch[2] += gnd
    
    # Connect Arduino
    arduino["+5V"] += vcc5
    arduino["GND"] += gnd
    arduino["A0"] += current_sense    # Current sensor output
    arduino["A1"] += voltage_monitor  # Voltage divider output
    arduino["D2"] += proximity_out    # Proximity sensor output
    arduino["D7"] += switch_out       # Switch
    
    # Optional: Connect 12V to Arduino VIN (dashed line in diagram)
    # Comment out if not needed
    arduino["VIN"] += vcc12
    
    # Run ERC check to verify circuit
    # erc()
    
    # Generate netlist
    netlist_file = "viscosimeter.net"
    generate_netlist(file=netlist_file)
    print(f"Netlist generated successfully: {netlist_file}")
    
    # Generate a simple schematic text description
    print("\nViscosimeter Circuit Connections:")
    print("================================")
    print("Power Supply:")
    print(f"  12V Supply -> Current Sensor IP+")
    print(f"  12V Supply -> Voltage Divider R1 (top)")
    print(f"  12V Supply -> Arduino VIN (optional)")
    print(f"  5V from Arduino -> Current Sensor VCC, Proximity Sensor VCC")
    print(f"  GND common to all components")
    
    print("\nSignal Connections:")
    print(f"  Current Sensor VIOUT -> Arduino A0")
    print(f"  Voltage Divider (R1/R2 junction) -> Arduino A1")
    print(f"  Proximity Sensor OUT -> Arduino D2")
    print(f"  Switch -> Arduino D7")
    print(f"  Current Sensor IP- -> Motor (+)")
    print(f"  Motor (-) -> GND")
    
    print("\nComponent Details:")
    print(f"  Current Sensor: ACS712xLCTR-30A (±30A, 66mV/A)")
    print(f"  Motor: RS-445PA-14233R")
    print(f"  Proximity Sensor: TCD210245AA (3-pin: VCC, GND, OUT)")
    print(f"  Voltage Divider: 48.7kΩ / 31.4kΩ (for 12V monitoring)")
    
    return netlist_file

if __name__ == "__main__":
    # Call the function to create the circuit
    netlist_file = create_viscosimeter_circuit()
    print(f"\nTo create a visual schematic in KiCad:")
    print(f"1. Open KiCad and create a new project")
    print(f"2. Open the Schematic Editor")
    print(f"3. Go to File -> Import -> Netlist")
    print(f"4. Select the generated file: {netlist_file}")
    print(f"5. KiCad will place components that you can arrange according to the diagram")
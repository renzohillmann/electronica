"""
Main viscosimeter circuit script that creates a KiCad schematic file for the viscosimeter.
"""
# First, import the initialization script
import kicad_init

# Now import SKiDL and other modules
from skidl import *
import os
import json
import uuid
from datetime import datetime

# Set up SKiDL to use KiCad libraries
set_default_tool(KICAD)

def generate_kicad_schematic():
    """Generate a KiCad schematic file (.kicad_sch) with complete symbol definitions"""
    
    # Component positions
    component_positions = {
        "arduino": {"x": 127, "y": 76.2},
        "acs712": {"x": 76.2, "y": 50.8},
        "motor": {"x": 177.8, "y": 50.8},
        "prox_sensor": {"x": 76.2, "y": 101.6},
        "switch": {"x": 177.8, "y": 101.6},
        "pwr12v": {"x": 25.4, "y": 25.4},
        "r1": {"x": 50.8, "y": 25.4},
        "r2": {"x": 50.8, "y": 38.1}
    }
    
    # Generate KiCad S-expression format with complete symbol definitions
    schematic_content = f'''(kicad_sch (version 20230121) (generator eeschema)

  (uuid {str(uuid.uuid4())})

  (paper "A4")

  (lib_symbols
    (symbol "Device:R" (pin_numbers hide) (pin_names (offset 0)) (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "R" (at 0 0 90)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (at -1.778 0 90)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "R_0_1"
        (rectangle (start -1.016 -2.54) (end 1.016 2.54)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
      )
      (symbol "R_1_1"
        (pin passive line (at 0 3.81 270) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 0 -3.81 90) (length 1.27)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
    (symbol "Connector:Screw_Terminal_01x02" (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 2.54 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Screw_Terminal_01x02" (at 0 -5.08 0)
        (effects (font (size 1.27 1.27)))
      )
      (symbol "Screw_Terminal_01x02_1_1"
        (rectangle (start -1.27 1.27) (end 1.27 -3.81)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (circle (center 0 0) (radius 0.635)
          (stroke (width 0.1524) (type default))
          (fill (type none))
        )
        (circle (center 0 -2.54) (radius 0.635)
          (stroke (width 0.1524) (type default))
          (fill (type none))
        )
        (pin passive line (at -5.08 0 0) (length 3.81)
          (name "Pin_1" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -5.08 -2.54 0) (length 3.81)
          (name "Pin_2" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
    (symbol "Connector:Screw_Terminal_01x03" (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 3.81 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Screw_Terminal_01x03" (at 0 -6.35 0)
        (effects (font (size 1.27 1.27)))
      )
      (symbol "Screw_Terminal_01x03_1_1"
        (rectangle (start -1.27 2.54) (end 1.27 -5.08)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (circle (center 0 1.27) (radius 0.635)
          (stroke (width 0.1524) (type default))
          (fill (type none))
        )
        (circle (center 0 -1.27) (radius 0.635)
          (stroke (width 0.1524) (type default))
          (fill (type none))
        )
        (circle (center 0 -3.81) (radius 0.635)
          (stroke (width 0.1524) (type default))
          (fill (type none))
        )
        (pin passive line (at -5.08 1.27 0) (length 3.81)
          (name "Pin_1" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -5.08 -1.27 0) (length 3.81)
          (name "Pin_2" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -5.08 -3.81 0) (length 3.81)
          (name "Pin_3" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
      )
    )
    (symbol "Switch:SW_Push" (pin_numbers hide) (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "SW" (at 1.27 2.54 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (property "Value" "SW_Push" (at 0 -1.524 0)
        (effects (font (size 1.27 1.27)))
      )
      (symbol "SW_Push_0_1"
        (circle (center -2.032 0) (radius 0.508)
          (stroke (width 0) (type default))
          (fill (type none))
        )
        (polyline
          (pts
            (xy 0 1.27)
            (xy 0 3.048)
          )
          (stroke (width 0) (type default))
          (fill (type none))
        )
        (polyline
          (pts
            (xy 2.54 1.27)
            (xy -2.54 1.27)
          )
          (stroke (width 0) (type default))
          (fill (type none))
        )
        (circle (center 2.032 0) (radius 0.508)
          (stroke (width 0) (type default))
          (fill (type none))
        )
        (pin passive line (at -5.08 0 0) (length 2.54)
          (name "1" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 5.08 0 180) (length 2.54)
          (name "2" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
    (symbol "MCU_Module:Arduino_UNO_R3" (in_bom yes) (on_board yes)
      (property "Reference" "A" (at -10.16 23.495 0)
        (effects (font (size 1.27 1.27)) (justify left bottom))
      )
      (property "Value" "Arduino_UNO_R3" (at 5.08 -26.67 0)
        (effects (font (size 1.27 1.27)) (justify left top))
      )
      (symbol "Arduino_UNO_R3_0_1"
        (rectangle (start -15.24 22.86) (end 15.24 -25.4)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
      )
      (symbol "Arduino_UNO_R3_1_1"
        (pin bidirectional line (at -17.78 15.24 0) (length 2.54)
          (name "A0" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at -17.78 12.7 0) (length 2.54)
          (name "A1" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at 17.78 5.08 180) (length 2.54)
          (name "D2" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
        (pin bidirectional line (at 17.78 -10.16 180) (length 2.54)
          (name "D7" (effects (font (size 1.27 1.27))))
          (number "4" (effects (font (size 1.27 1.27))))
        )
        (pin power_out line (at -2.54 25.4 270) (length 2.54)
          (name "+5V" (effects (font (size 1.27 1.27))))
          (number "5" (effects (font (size 1.27 1.27))))
        )
        (pin power_in line (at 0 -27.94 90) (length 2.54)
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "6" (effects (font (size 1.27 1.27))))
        )
        (pin power_in line (at -5.08 25.4 270) (length 2.54)
          (name "VIN" (effects (font (size 1.27 1.27))))
          (number "7" (effects (font (size 1.27 1.27))))
        )
      )
    )
    (symbol "Motor:Motor_DC" (pin_names (offset 0) hide) (in_bom yes) (on_board yes)
      (property "Reference" "M" (at 2.54 2.54 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (property "Value" "Motor_DC" (at 2.54 -5.08 0)
        (effects (font (size 1.27 1.27)) (justify left top))
      )
      (symbol "Motor_DC_0_0"
        (polyline
          (pts
            (xy -1.27 -3.302)
            (xy -1.27 0.508)
            (xy 0 -1.397)
            (xy 1.27 0.508)
            (xy 1.27 -3.302)
          )
          (stroke (width 0) (type default))
          (fill (type none))
        )
        (circle (center 0 -1.397) (radius 3.2004)
          (stroke (width 0.254) (type default))
          (fill (type none))
        )
        (pin passive line (at 0 2.54 270) (length 1.905)
          (name "+" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 0 -5.08 90) (length 1.143)
          (name "-" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
    (symbol "Sensor_Current:ACS712xLCTR-30A" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at -10.16 8.89 0)
        (effects (font (size 1.27 1.27)) (justify right))
      )
      (property "Value" "ACS712xLCTR-30A" (at 1.27 8.89 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (symbol "ACS712xLCTR-30A_0_1"
        (rectangle (start -10.16 7.62) (end 10.16 -7.62)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
      )
      (symbol "ACS712xLCTR-30A_1_1"
        (pin power_in line (at 0 10.16 270) (length 2.54)
          (name "VCC" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin power_in line (at 0 -10.16 90) (length 2.54)
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin output line (at 12.7 0 180) (length 2.54)
          (name "VIOUT" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -12.7 2.54 0) (length 2.54)
          (name "IP+" (effects (font (size 1.27 1.27))))
          (number "4" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -12.7 -2.54 0) (length 2.54)
          (name "IP-" (effects (font (size 1.27 1.27))))
          (number "5" (effects (font (size 1.27 1.27))))
        )
      )
    )
  )

  (wire (pts (xy {component_positions["pwr12v"]["x"] + 3.81} {component_positions["pwr12v"]["y"]}) (xy {component_positions["r1"]["x"]} {component_positions["r1"]["y"] + 3.81}))
    (stroke (width 0) (type default))
    (uuid {str(uuid.uuid4())})
  )
  
  (wire (pts (xy {component_positions["r1"]["x"]} {component_positions["r1"]["y"] - 3.81}) (xy {component_positions["r2"]["x"]} {component_positions["r2"]["y"] + 3.81}))
    (stroke (width 0) (type default))
    (uuid {str(uuid.uuid4())})
  )

  (symbol (lib_id "MCU_Module:Arduino_UNO_R3") (at {component_positions["arduino"]["x"]} {component_positions["arduino"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "A1" (at {component_positions["arduino"]["x"]} {component_positions["arduino"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "Arduino_UNO_R3" (at {component_positions["arduino"]["x"]} {component_positions["arduino"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "Module:Arduino_UNO_R3" (at {component_positions["arduino"]["x"]} {component_positions["arduino"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "https://www.arduino.cc/en/Main/arduinoBoardUno" (at {component_positions["arduino"]["x"]} {component_positions["arduino"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "A0" (uuid {str(uuid.uuid4())}))
    (pin "A1" (uuid {str(uuid.uuid4())}))
    (pin "D2" (uuid {str(uuid.uuid4())}))
    (pin "D7" (uuid {str(uuid.uuid4())}))
    (pin "+5V" (uuid {str(uuid.uuid4())}))
    (pin "GND" (uuid {str(uuid.uuid4())}))
    (pin "VIN" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "A1") (unit 1))
      )
    )
  )

  (symbol (lib_id "Sensor_Current:ACS712xLCTR-30A") (at {component_positions["acs712"]["x"]} {component_positions["acs712"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "U1" (at {component_positions["acs712"]["x"]} {component_positions["acs712"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "ACS712xLCTR-30A" (at {component_positions["acs712"]["x"]} {component_positions["acs712"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at {component_positions["acs712"]["x"]} {component_positions["acs712"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "VCC" (uuid {str(uuid.uuid4())}))
    (pin "GND" (uuid {str(uuid.uuid4())}))
    (pin "VIOUT" (uuid {str(uuid.uuid4())}))
    (pin "IP+" (uuid {str(uuid.uuid4())}))
    (pin "IP-" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "U1") (unit 1))
      )
    )
  )

  (symbol (lib_id "Motor:Motor_DC") (at {component_positions["motor"]["x"]} {component_positions["motor"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "M1" (at {component_positions["motor"]["x"]} {component_positions["motor"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "RS-445PA-14233R" (at {component_positions["motor"]["x"]} {component_positions["motor"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal" (at {component_positions["motor"]["x"]} {component_positions["motor"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "+" (uuid {str(uuid.uuid4())}))
    (pin "-" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "M1") (unit 1))
      )
    )
  )

  (symbol (lib_id "Connector:Screw_Terminal_01x03") (at {component_positions["prox_sensor"]["x"]} {component_positions["prox_sensor"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "J1" (at {component_positions["prox_sensor"]["x"]} {component_positions["prox_sensor"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "TCD210245AA" (at {component_positions["prox_sensor"]["x"]} {component_positions["prox_sensor"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at {component_positions["prox_sensor"]["x"]} {component_positions["prox_sensor"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "1" (uuid {str(uuid.uuid4())}))
    (pin "2" (uuid {str(uuid.uuid4())}))
    (pin "3" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "J1") (unit 1))
      )
    )
  )

  (symbol (lib_id "Switch:SW_Push") (at {component_positions["switch"]["x"]} {component_positions["switch"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "SW1" (at {component_positions["switch"]["x"]} {component_positions["switch"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "SW_Push" (at {component_positions["switch"]["x"]} {component_positions["switch"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "Button_Switch_THT:SW_PUSH_6mm" (at {component_positions["switch"]["x"]} {component_positions["switch"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "1" (uuid {str(uuid.uuid4())}))
    (pin "2" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "SW1") (unit 1))
      )
    )
  )

  (symbol (lib_id "Connector:Screw_Terminal_01x02") (at {component_positions["pwr12v"]["x"]} {component_positions["pwr12v"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "J2" (at {component_positions["pwr12v"]["x"]} {component_positions["pwr12v"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "12V_Supply" (at {component_positions["pwr12v"]["x"]} {component_positions["pwr12v"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at {component_positions["pwr12v"]["x"]} {component_positions["pwr12v"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "1" (uuid {str(uuid.uuid4())}))
    (pin "2" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "J2") (unit 1))
      )
    )
  )

  (symbol (lib_id "Device:R") (at {component_positions["r1"]["x"]} {component_positions["r1"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "R1" (at {component_positions["r1"]["x"]} {component_positions["r1"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "48.7k" (at {component_positions["r1"]["x"]} {component_positions["r1"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at {component_positions["r1"]["x"]} {component_positions["r1"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "1" (uuid {str(uuid.uuid4())}))
    (pin "2" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "R1") (unit 1))
      )
    )
  )

  (symbol (lib_id "Device:R") (at {component_positions["r2"]["x"]} {component_positions["r2"]["y"]} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (fields_autoplaced)
    (uuid {str(uuid.uuid4())})
    (property "Reference" "R2" (at {component_positions["r2"]["x"]} {component_positions["r2"]["y"] - 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "31.4k" (at {component_positions["r2"]["x"]} {component_positions["r2"]["y"] + 7.62} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at {component_positions["r2"]["x"]} {component_positions["r2"]["y"]} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (pin "1" (uuid {str(uuid.uuid4())}))
    (pin "2" (uuid {str(uuid.uuid4())}))
    (instances
      (project "viscosimeter"
        (path "/" (reference "R2") (unit 1))
      )
    )
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)'''
    
    return schematic_content

def create_viscosimeter_circuit():
    """Creates the viscosimeter circuit and generates both netlist and schematic files"""
    
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
    arduino["VIN"] += vcc12
    
    # Generate netlist
    netlist_file = "viscosimeter.net"
    generate_netlist()
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

    # Generate KiCad schematic file with proper S-expression format
    schematic_file = "viscosimeter.kicad_sch"
    schematic_content = generate_kicad_schematic()
    
    with open(schematic_file, 'w') as f:
        f.write(schematic_content)
    
    print(f"KiCad schematic file generated: {schematic_file}")
    
    return netlist_file, schematic_file

if __name__ == "__main__":
    # Call the function to create the circuit
    netlist_file, schematic_file = create_viscosimeter_circuit()
    print(f"\nTo open the schematic in KiCad:")
    print(f"1. Open KiCad and create a new project")
    print(f"2. Copy the generated file '{schematic_file}' to your project folder")
    print(f"3. Open the schematic file directly in KiCad")
    print(f"4. The components will be placed with basic positioning")
    print(f"5. You can rearrange components and add wires as needed")
from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

viscosimeter_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'R'}), 'ref_prefix':'R', 'fplist':[''], 'footprint':'Resistor_SMD:R_0805_2012Metric', 'keywords':'R res resistor', 'description':'', 'datasheet':'~', 'pins':[
            Pin(num='1',name='~',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='~',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ACS712xLCTR-30A', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ACS712xLCTR-30A'}), 'ref_prefix':'U', 'fplist':['Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm'], 'footprint':'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'keywords':'hall effect current monitor sensor isolated', 'description':'', 'datasheet':'http://www.allegromicro.com/~/media/Files/Datasheets/ACS712-Datasheet.ashx?la=en', 'pins':[
            Pin(num='1',name='IP+',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='IP+',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='IP-',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='IP-',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='VCC',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='7',name='VIOUT',func=pin_types.OUTPUT,unit=1),
            Pin(num='6',name='FILTER',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'Motor_DC', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'Motor_DC'}), 'ref_prefix':'M', 'fplist':[''], 'footprint':'TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal', 'keywords':'DC Motor', 'description':'', 'datasheet':'~', 'pins':[
            Pin(num='1',name='+',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='-',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'Screw_Terminal_01x03', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'Screw_Terminal_01x03'}), 'ref_prefix':'J', 'fplist':[''], 'footprint':'TerminalBlock:TerminalBlock_bornier-3_P5.08mm', 'keywords':'screw terminal', 'description':'', 'datasheet':'~', 'pins':[
            Pin(num='1',name='Pin_1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='Pin_2',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='Pin_3',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'SW_Push', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'SW_Push'}), 'ref_prefix':'SW', 'fplist':[''], 'footprint':'Button_Switch_THT:SW_PUSH_6mm', 'keywords':'switch normally-open pushbutton push-button', 'description':'', 'datasheet':'~', 'pins':[
            Pin(num='1',name='1',func=pin_types.PASSIVE),
            Pin(num='2',name='2',func=pin_types.PASSIVE)], 'unit_defs':[] }),
        Part(**{ 'name':'Arduino_UNO_R3', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'Arduino_UNO_R3'}), 'ref_prefix':'A', 'fplist':['Module:Arduino_UNO_R3'], 'footprint':'Module:Arduino_UNO_R3', 'keywords':'Arduino UNO R3 Microcontroller Module Atmel AVR USB', 'description':'', 'datasheet':'https://www.arduino.cc/en/Main/arduinoBoardUno', 'pins':[
            Pin(num='15',name='D0/RX',func=pin_types.BIDIR,unit=1),
            Pin(num='16',name='D1/TX',func=pin_types.BIDIR,unit=1),
            Pin(num='17',name='D2',func=pin_types.BIDIR,unit=1),
            Pin(num='18',name='D3',func=pin_types.BIDIR,unit=1),
            Pin(num='19',name='D4',func=pin_types.BIDIR,unit=1),
            Pin(num='20',name='D5',func=pin_types.BIDIR,unit=1),
            Pin(num='21',name='D6',func=pin_types.BIDIR,unit=1),
            Pin(num='22',name='D7',func=pin_types.BIDIR,unit=1),
            Pin(num='23',name='D8',func=pin_types.BIDIR,unit=1),
            Pin(num='24',name='D9',func=pin_types.BIDIR,unit=1),
            Pin(num='25',name='D10',func=pin_types.BIDIR,unit=1),
            Pin(num='26',name='D11',func=pin_types.BIDIR,unit=1),
            Pin(num='27',name='D12',func=pin_types.BIDIR,unit=1),
            Pin(num='28',name='D13',func=pin_types.BIDIR,unit=1),
            Pin(num='1',name='NC',func=pin_types.NOCONNECT,unit=1),
            Pin(num='8',name='VIN',func=pin_types.PWRIN,unit=1),
            Pin(num='29',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='6',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='3V3',func=pin_types.PWROUT,unit=1),
            Pin(num='7',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='+5V',func=pin_types.PWROUT,unit=1),
            Pin(num='3',name='~{RESET}',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='IOREF',func=pin_types.OUTPUT,unit=1),
            Pin(num='30',name='AREF',func=pin_types.INPUT,unit=1),
            Pin(num='9',name='A0',func=pin_types.BIDIR,unit=1),
            Pin(num='10',name='A1',func=pin_types.BIDIR,unit=1),
            Pin(num='11',name='A2',func=pin_types.BIDIR,unit=1),
            Pin(num='12',name='A3',func=pin_types.BIDIR,unit=1),
            Pin(num='13',name='SDA/A4',func=pin_types.BIDIR,unit=1),
            Pin(num='14',name='SCL/A5',func=pin_types.BIDIR,unit=1),
            Pin(num='31',name='SDA/A4',func=pin_types.BIDIR,unit=1),
            Pin(num='32',name='SCL/A5',func=pin_types.BIDIR,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'Screw_Terminal_01x02', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'Screw_Terminal_01x02'}), 'ref_prefix':'J', 'fplist':[''], 'footprint':'TerminalBlock:TerminalBlock_bornier-2_P5.08mm', 'keywords':'screw terminal', 'description':'', 'datasheet':'~', 'pins':[
            Pin(num='1',name='Pin_1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='Pin_2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] })])
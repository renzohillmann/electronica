"""
KiCad environment initialization script.
Run this script before importing any SKiDL modules to set up the environment.
"""
import os
import sys

def initialize_kicad_env():
    """Set up KiCad environment variables before any imports."""
    # Set KiCad directory paths
    kicad_dir = r"C:\Users\RenzoStefanoHillmann\AppData\Local\Programs\KiCad\9.0"
    kicad_symbol_dir = os.path.join(kicad_dir, "share", "kicad", "symbols")
    
    # Set all required environment variables
    os.environ["KICAD_SYMBOL_DIR"] = kicad_symbol_dir
    os.environ["KICAD9_SYMBOL_DIR"] = kicad_symbol_dir
    os.environ["KICAD8_SYMBOL_DIR"] = kicad_symbol_dir  # For backward compatibility
    os.environ["KICAD7_SYMBOL_DIR"] = kicad_symbol_dir  # For backward compatibility
    os.environ["KICAD6_SYMBOL_DIR"] = kicad_symbol_dir  # For backward compatibility
    
    print("KiCad environment variables set successfully:")
    print(f"  KICAD_SYMBOL_DIR = {os.environ['KICAD_SYMBOL_DIR']}")
    return True

# Run initialization when this script is imported
initialize_kicad_env()
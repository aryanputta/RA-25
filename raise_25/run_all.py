
import os
import subprocess
import sys

def run_all():
    script_dir = os.path.join(os.path.dirname(__file__), 'scripts')
    scripts = [
        'section_3_attention.py',
        'section_5_scaling.py',
        'section_5b_emergence.py',
        'section_6_forecast.py',
        'section_7_trust.py',
        'section_8_economic.py'
    ]
    
    print("--- Generating Raise 25 Research Figures ---")
    for script in scripts:
        print(f"Running {script}...")
        try:
            subprocess.check_call([sys.executable, os.path.join(script_dir, script)])
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")
            
    print("--- Done. Figures are in /figures. ---")

if __name__ == "__main__":
    run_all()

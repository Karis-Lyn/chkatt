import json
import os

def read_pfile(fnam, pfile):
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    prev_dir = os.path.dirname(curr_dir)
    final_dir = f"{prev_dir}/{pfile}/{fnam}"
    
    
    if os.path.exists(final_dir):
        with open(final_dir) as f:
            return json.load(f)



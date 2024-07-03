import os
from ray.rllib.algorithms.algorithm import Algorithm

def save_algo(algo, name):
    base_dir = os.path.join(os.getcwd(), "algos")
    subfolder_path = os.path.join(base_dir, name)
    os.makedirs(subfolder_path, exist_ok=True)
    path_to_checkpoint  = algo.save(subfolder_path)
    print(f"An Algorithm checkpoint has been created inside directory: '{path_to_checkpoint}'.")

def load_algo(name):
    base_dir = os.path.join(os.getcwd(), "algos")
    subfolder_path = os.path.join(base_dir, name)
    if not os.path.exists(subfolder_path):
        raise FileNotFoundError(f"The specified subfolder '{subfolder_path}' does not exist.")
    
    return Algorithm.from_checkpoint(subfolder_path)
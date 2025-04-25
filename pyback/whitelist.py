import importlib
import os
from pyback.registry import register_method

def register_all_methods():
    methods_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../apps/methods')
    
    if not os.path.exists(methods_folder):
        raise FileNotFoundError(f"The 'methods' folder was not found at: {methods_folder}")
    
    for filename in os.listdir(methods_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"apps.methods.{filename[:-3]}"
            module = importlib.import_module(module_name)
            
            for name, obj in module.__dict__.items():
                if callable(obj):
                    register_method(name, obj)
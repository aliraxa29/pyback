import importlib
import os
from fastapi import HTTPException
from pyback.registry import register_model
from pyback.model import DocType

def register_all_models():
    apps_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../apps')
    if not os.path.exists(apps_folder):
        raise FileNotFoundError(f"The 'apps' folder was not found at: {apps_folder}")
    
    for filename in os.listdir(apps_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"apps.{filename[:-3]}"
            module = importlib.import_module(module_name)
            
            for name, obj in module.__dict__.items():
                if isinstance(obj, type) and issubclass(obj, DocType):
                    register_model(name.lower(), obj)


def get_model(doctype: str):
    """
    Dynamically imports and retrieves the model class corresponding to the doctype.
    
    Args:
        doctype (str): The doctype name for which we need to load the model class.
        
    Returns:
        Type: The model class corresponding to the doctype.
        
    Raises:
        HTTPException: If the model corresponding to the doctype is not found.
    """
    doctype_lower = doctype.lower().replace(" ", "_")
    model_name = doctype.replace(" ", "")

    try:
        module = importlib.import_module(f"apps.models.{doctype_lower}")
        model_class = getattr(module, model_name)
        return model_class
    except (ModuleNotFoundError, AttributeError) as e:
        raise HTTPException(status_code=404, detail=f"Model for doctype '{doctype}' not found")

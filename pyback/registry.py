model_registry = {}
method_registry = {}

def register_model(name: str, model_class):
    model_registry[name.lower()] = model_class

def get_model(name: str):
    return model_registry.get(name.lower())


def register_method(name: str, method):
    """
    Register a method to the method registry.
    
    Parameters:
    - name (str): The name of the method to be used in the URL
    - method (callable): The actual function or method to be registered
    """
    method_registry[name] = method

def get_registered_method(name: str):
    """
    Retrieve a registered method from the method registry.
    
    Parameters:
    - name (str): The name of the method to retrieve
    
    Returns:
    - callable: The method if found, else None
    """
    return method_registry.get(name)
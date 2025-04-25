from fastapi import APIRouter, HTTPException
from pyback.whitelist import register_all_methods

router = APIRouter()

register_all_methods()

@router.post("/api/method/{method_name}")
async def call_method(method_name: str, params: dict):
    try:
        method = globals().get(method_name)  # Get method from globals
        if not method:
            raise HTTPException(status_code=404, detail="Method not found")
        
        result = method(**params)  # Call the method with parameters
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

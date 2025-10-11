from datetime import datetime

def DtoResponse(success=True, message="", data=None, status=200):
    response = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "success": success,
        "message": message,
        "data": data,
        "status": status
    }
    
    return response
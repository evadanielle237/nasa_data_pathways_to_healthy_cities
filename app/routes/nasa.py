from fastapi import APIRouter
from app.services import nasa_service

# Create a router for NASA-related endpoints
router = APIRouter() #router

@router.get("/land-use")
def get_land_use_data():
    """
    Example endpoint to fetch NASA land use data.
    Later, this will call real NASA APIs and return processed results.
    """
    data = nasa_service.fetch_land_use()
    return {"status": "success", "data": data}
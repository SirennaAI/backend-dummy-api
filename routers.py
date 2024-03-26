from datetime import datetime
from core.dummy_data import generate_call_data
from fastapi import APIRouter, Query
router = APIRouter()
call_type_pattern = "^(inbound|outbound)$"

@router.get("/calls/")
async def get_calls(
    start_date: datetime = Query(..., description="Start date in format YYYY-MM-DD HH:MM:SS"),
    end_date: datetime = Query(..., description="End date in format YYYY-MM-DD HH:MM:SS"),
    limit: int = Query(10, ge=1, le=100, description="Results limit per page"),
    page: int = Query(1, ge=1, description="Page number"),
   call_type: str = Query(None, regex="^(inbound|outbound)$", description="Type of call (inbound/outbound)")
):

    calls =await generate_call_data(start_date, end_date, call_type, limit,page)
    return calls
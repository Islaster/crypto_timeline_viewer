import httpx
from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

@router.get("/historical/{coin_id}")
async def get_historical_prices(coin_id: str = "bitcoin", days: int = 30):
    """
    Fetch historical price data from CoinGecko
    """
    url = f"{COINGECKO_API_URL}/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": days}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()

    data = response.json()
    return {
        "prices": data["prices"]  # each entry is [timestamp, price]
    }


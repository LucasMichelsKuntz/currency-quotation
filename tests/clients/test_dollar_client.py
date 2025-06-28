import pytest
import httpx
from app.clients.dollar_client import DollarClient

@pytest.mark.asyncio
async def test_fetch_success(monkeypatch):
    async def mock_get(self,url):
        request = httpx.Request("GET", url)
        return httpx.Response(
            status_code=200,
            json={
                "currency_price": "650",
                "currency_name": "DOLLAR",
                "currency_kind": "USD",
                "currency_formatter": "decimal"
            },
            request=request
        )

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    client = DollarClient(base_url="http://fake-url")
    result = await client.fetch()

    assert result.currency == "DOLLAR"
    assert result.value == 6.50

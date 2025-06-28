import pytest
import httpx
from app.clients.euro_client import EuroClient
from app.models.euro_model import EuroResponse

@pytest.mark.asyncio
async def test_fetch_success(monkeypatch):
    async def mock_get(self,url):
        request = httpx.Request("GET", url)
        return httpx.Response(
            status_code=200,
            json={
                "cotacao": {
                    "moeda": "EURO",
                    "sigla": "EUR",
                    "valor_comercial": 6.9
                }
            },
            request=request  
        )

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    client = EuroClient(base_url="http://fake-url")
    result = await client.fetch()

    assert result.currency == "EURO"
    assert result.value == 6.9

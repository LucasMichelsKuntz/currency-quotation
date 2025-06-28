import pytest
from unittest.mock import AsyncMock
from app.services.euro_service import EuroService
from app.entities.quotation import Quotation

@pytest.mark.asyncio
async def test_get_quotation_returns_quotation():
    mock_client = AsyncMock()
    mock_client.fetch.return_value = Quotation(currency="EURO", value=6.9)
    
    service = EuroService(client=mock_client)
    quotation = await service.get_quotation()
    
    assert quotation.currency == "EURO"
    assert quotation.value == 6.9

import pytest
from unittest.mock import AsyncMock
from app.services.dollar_service import DollarService
from app.entities.quotation import Quotation

@pytest.mark.asyncio
async def test_get_quotation_returns_quotation():
    mock_client = AsyncMock()
    mock_client.fetch.return_value = Quotation(currency="DOLLAR", value=6.9)
    
    service = DollarService(client=mock_client)
    quotation = await service.get_quotation()
    
    assert quotation.currency == "DOLLAR"
    assert quotation.value == 6.9

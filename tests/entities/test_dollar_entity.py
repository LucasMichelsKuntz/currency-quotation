from decimal import Decimal
from app.entities.dollar import Dollar

def test_to_quotation():
    dollar = Dollar(
        currency_price=Decimal("6.50"),
        currency_name="DOLLAR",
        currency_kind="USD",
        currency_formatter="decimal"
    )

    quotation = dollar.to_quotation()

    assert quotation.currency == "DOLLAR"
    assert quotation.value == 6.50

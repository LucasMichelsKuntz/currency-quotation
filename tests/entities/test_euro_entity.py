from decimal import Decimal
from app.entities.euro import Euro
from app.entities.quotation import Quotation

def test_to_quotation():
    euro = Euro(
        valor_comercial=Decimal("6.9"),
        sigla="EUR",
        moeda="EURO"
    )
    quotation = euro.to_quotation()

    assert isinstance(quotation, Quotation)
    assert quotation.currency == "EURO"
    assert quotation.value == 6.9

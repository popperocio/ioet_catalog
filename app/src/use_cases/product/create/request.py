from decimal import Decimal

from typing import NamedTuple

from ....core import ProductStatuses


class CreateProductRequest(NamedTuple):
  product_id: str
  user_id: str
  name: str
  description: str | None
  price: Decimal
  location: str
  status: ProductStatuses
  is_available: bool

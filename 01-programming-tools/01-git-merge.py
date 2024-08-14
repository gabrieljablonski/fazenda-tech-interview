def calculate_total(price, tax_rate, decimal_places=2):
  total = (1 + tax_rate) * price
  return round(total, decimal_places)

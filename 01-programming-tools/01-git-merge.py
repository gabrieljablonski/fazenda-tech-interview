def calculate_total(price, tax_rate, discount_rate=0):
  total = (1 + tax_rate - discount_rate) * price
  return total

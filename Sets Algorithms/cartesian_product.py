
def cartesianProduct(setA, setB):

  if len(setA) == 0:
    return None

  if len(setB) == 0:
    return None

  product = []
  for elementA in setA:
    for elementB in setB:
      product.append([elementA, elementB])

  return product

print(cartesianProduct(['a', 'b'], ['1', '2', '3']))
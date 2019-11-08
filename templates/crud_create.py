def crud_create(iban, bank, holders, account_id, kind, number, swift_bic):
  """
    Returns an account dict given a set of paramaters.
  """
  return {
    'IBAN': iban,
    'bank': bank,
    'holders': holders,
    'id': account_id,
    'kind': kind,
    'number': number,
    'swift_bic': swift_bic
  }
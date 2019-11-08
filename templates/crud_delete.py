def crud_delete(accounts, index_to_delete):
  print(f"Deleted: {accounts.pop(index_to_delete)}")
  return accounts
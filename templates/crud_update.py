from .crud_read import crud_read
def crud_update(account, user):
  """
  Takes the name of a file, <account> and a user dict <user> then returns the combined list
  """
  account_list = []
  account_list.append(crud_read(account))
  account_list.append(user)
  return account_list
from templates.crud_read import crud_read
from templates.crud_create import crud_create
from templates.crud_update import crud_update
from templates.crud_delete import crud_delete
from templates.crud_save import crud_save

crud_read('accounts.json')
user = crud_create(None, {}, [], 'checking-kids-bob', 'checking', '123456-12345678', None)
accounts = crud_update('accounts.json', user)
crud_delete(accounts, 0)

user = crud_create(None, {}, [], 'savings-kids-bobby', 'savings', '654321-87654321', None)

crud_save(accounts)






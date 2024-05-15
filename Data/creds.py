
HOSTS = {
    "backoffice": "some admin host",
    "frontoffice": "https://sanor.ltd/"
}

# URL list store
URLS = {
    "FO login page": f'{HOSTS["frontoffice"]}/account/login'
}


# In case of DB tests
db_host_some = 'some host'
db_name_some = 'some name'
db_user_some = 'some user'
db_pass_some = 'some pass'
# connection = pg8000.native.Connection(db_user_some, password=db_pass_some, host=db_host_some, database=db_name_some)
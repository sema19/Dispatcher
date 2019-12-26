import configparser

settings = configparser.ConfigParser()
settings.read("config.ini")

def basic_auth(username,password,required_scopes=None):
	un=settings.get("auth","user")
	pw=settings.get("auth","password")
	if username==un and password ==pw:
		info = {'sub':un, 'scope': 'secret'}
		return info
	else:
		return 500

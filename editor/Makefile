# Create dev env
env_create:
	virtualenv --distribute --no-site-packages apps

# Freeze libraries in env
env_freeze:
	pip freeze > requirements.txt

# Upgrade the env with requirements file
env_upgrade:
	pip install -r requirements.txt

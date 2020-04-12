test:
	pytest

setup-dev-env:
	sudo apt install -y python3 python3-pip virtualenv

clean:
	py3clean .

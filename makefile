test:
	pytest

setup-ubuntu-dev:
	sudo apt install -y python3 python3-pip virtualenv
	pip3 install pytest sphinx

clean:
	py3clean .
	pyclean .

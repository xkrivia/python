test:
	pytest -v
	# pep8 ~ not ready yet but the end goal

setup-ubuntu-dev:
	sudo apt install -y python3 python3-pip virtualenv
	pip3 install pytest sphinx pep8 flake8

clean:
	py3clean .
	pyclean .
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf	

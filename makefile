release:
	mkdir -p logs
	python3 -m pytest -v
	tree -C logs

setup-ubuntu-dev-env:
	sudo apt install -y python3 python3-pip virtualenv
	sudo apt install -y tree
	sudo apt install -y xsel xclip
	sudo apt install -y python-autopep8
	sudo -H pip3 install pytest sphinx pep8 flake8
	sudo -H pip3 install pyperclip arrow

clean-artifacts:
	py3clean .
	pyclean .
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf

clean-logs:
	find . | grep -E "(logs|\.log)" | xargs rm -rf
	tree -C logs

autopep8:
	find . -name '*.py' -exec autopep8 --in-place '{}' \;

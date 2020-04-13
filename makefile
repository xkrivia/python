test:
	mkdir -p logs
	python3 -m pytest -v

setup-ubuntu:
	sudo apt install -y python3 python3-pip virtualenv
	sudo apt install -y xsel xclip
	sudo -H pip3 install pytest sphinx pep8 flake8
	sudo -H pip3 install pyperclip

clean:
	py3clean .
	pyclean .
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf	
	find . | grep -E "(logs|\.log)" | xargs rm -rf	

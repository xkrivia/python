release:
	mkdir -p logs
	python3 -m pytest -v
	tree -C logs

ubuntu-dev-env-sane:
	sudo apt install -y python3 python3-pip virtualenv tree xsel xclip python-autopep8
	sudo -H pip3 install pytest sphinx pep8 flake8 pyperclip arrow

clean:
	py3clean . && pyclean .
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf

logs-go-away:
	find . | grep -E "(logs|\.log)" | xargs rm -rf
	tree -C logs

all-the-files-formatted:
	find . -name '*.py' -exec autopep8 --in-place '{}' \;

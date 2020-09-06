release:
	python3 -m pytest -v

ubuntu-dev-env-sane:
	sudo apt install -y python3 python3-pip virtualenv tree xsel xclip python3-autopep8
	sudo -H pip3 install pytest sphinx pep8 flake8 pyperclip arrow

clean:
	py3clean . #cleanup and old python cleanup.
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf #pseudo-hacky method to conditionally delete python files

logs-go-away:
	find . | grep -E "(logs|\.log)" | xargs rm -rf

python-pep8-formatted:
	find . -name '*.py' -exec autopep8 --in-place '{}' \;

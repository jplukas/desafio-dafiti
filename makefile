help:
	@echo "Essa é uma mensagem de ajuda."

lint: 
	@pylint mysite/ myblog/ --disable=C0115,C0116,C0114

format:
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa mysite/ myblog/
	@black -S -t py38 -l 79 mysite/ myblog --exclude '/(\.git|\.venv|env|venv|build|dist)/'

test:
	pytest
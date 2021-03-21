help:
	@echo "Essa é uma mensagem de ajuda."

format:
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa .
	@black -S -t py38 -l 79 . --exclude '/(\.git|\.venv|env|venv|build|dist)/'
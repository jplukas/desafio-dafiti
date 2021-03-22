help: ## Mostra essa mensagem de ajuda
	@awk 'BEGIN {FS = ":.?## "} /^[a-zA-Z_-]+:.?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

lint: ## Roda o pylint
	@pylint mysite/ myblog/ --disable=C0115,C0116,C0114

format: ## Formata o código usando isort e black
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa mysite/ myblog/
	@black -S -t py38 -l 79 mysite/ myblog --exclude '/(\.git|\.venv|env|venv|build|dist)/'

test: ## Roda os testes 
	@pytest -v
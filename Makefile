help: ## Mostra essa mensagem de ajuda
	@awk 'BEGIN {FS = ":.?## "} /^[a-zA-Z_-]+:.?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

lint: ## Roda o pylint
	@pylint blog/* --rcfile=.pylintrc

format: ## Formata o código usando isort e black
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa blog/
	@black -S -t py38 -l 79 blog/ --exclude '/(\.git|\.venv|env|venv|build|dist)/'

test: ## Roda os testes 
	@pytest -v

runserver: ## Inicia o servidor de desenvolvimento
	@echo "Iniciando servidor de desenvolvimento..."
	@python ./blog/manage.py runserver
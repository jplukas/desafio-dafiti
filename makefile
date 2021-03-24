help: ## Mostra essa mensagem de ajuda
	@awk 'BEGIN {FS = ":.?## "} /^[a-zA-Z_-]+:.?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

lint: clean  ## Roda o pylint
	@pylint blog --disable=C0115,C0116,C0114,C0103,C0415

format: ## Formata o código usando isort e black
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa blog
	@black -S -t py38 -l 79 blog --exclude '/(\.git|\.venv|env|venv|build|dist)/'

test: clean  ## Roda os testes 
	@pytest -v

clean: ## Exclui arquivos de cache
	@echo "Excluindo arquivos de cache"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -fr .pytest_cache/

prepare-run: clean
	@python blog/manage.py migrate
	@python blog/manage.py loaddata fixtures.json

run: clean ## Inicia o servidor de desenvolvimento
	@python blog/manage.py runserver
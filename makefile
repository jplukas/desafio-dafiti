help: ## Mostra essa mensagem de ajuda
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

lint: clean ## Roda o pylint
	@pylint blog --load-plugins=pylint_django --rcfile=pyproject.toml

format: ## Formata o código usando isort e black
	@isort blog --settings-file=pyproject.toml
	@black blog --config=pyproject.toml

test: clean ## Roda os testes 
	@pytest -v blog

clean: ## Exclui arquivos de cache
	@echo "Excluindo arquivos de cache"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -fr .pytest_cache/

preparations: docker-compose-up ## Pepara para rodar o servidor de desenvolvimento.
	@python blog/manage.py migrate

load-data: ## Carrega dados de teste no banco de dados
	@python blog/manage.py loaddata fixtures.json

run: clean ## Inicia o servidor de desenvolvimento. Precisa ter rodado make preparations uma vez antes
	@python blog/manage.py runserver

shell: ## Inicia um terminal interativo
	@python blog/manage.py shell

install-pip: ## Instala dependencias do pip
	@pip install -r requirements.txt

docker-compose-up: clean ## Up docker-compose for development
	@docker-compose up -d

docker-compose-stop: clean ## Stop docker-compose for development
	@docker-compose stop
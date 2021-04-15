FROM python:3.9
COPY blog/ /var/www/blog/
WORKDIR /var/www/blog/
COPY pyproject.toml pyproject.toml
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev --no-interaction --no-ansi
RUN curl -o ./file.zip "https://download.ckeditor.com/wordcount/releases/wordcount_1.17.9.zip"
RUN python -m zipfile -e ./file.zip wordcount/
RUN mv wordcount/wordcount/ /usr/local/lib/python3.9/site-packages/ckeditor/static/ckeditor/ckeditor/plugins/wordcount/
RUN rm -rf wordcount/
RUN rm -f file.zip
EXPOSE 8000
ENTRYPOINT ["./run.sh"]
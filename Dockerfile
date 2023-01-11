FROM python:3.9.5-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc curl g++ gnupg unixodbc-dev curl apt-transport-https

RUN pip install pipenv

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN  apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install --allow-unauthenticated -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN apt-get install -y unixodbc-dev


COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile

COPY ./app /app
COPY main.py /

EXPOSE 8001

WORKDIR /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
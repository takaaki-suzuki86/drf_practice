FROM python:3.10.5

# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# Poetryをインストール
RUN pip install poetry

# コンテナ内ではPython仮想環境の作成を無効
RUN poetry config virtualenvs.create false
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install

ADD . /code

# uWSGI起動
CMD uwsgi --ini ./.deploy/uwsgi.ini

FROM python:3.10.5

# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

#ADD _requirements.txt /code/
#RUN pip install -r _requirements.txt

# Poetryをインストール
RUN pip install poetry
#
## コンテナ内で仮想環境の作成を無効
RUN poetry config virtualenvs.create false
COPY ./pyproject.toml /code/pyproject.toml
RUN poetry install
#
CMD ["bash"]

ADD . /code/

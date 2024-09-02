FROM python:3.11

WORKDIR /code

COPY src/fishmlserv_git/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/Jeonghoon2/fishmlserv.git@0.3/api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
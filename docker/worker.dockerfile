FROM python:3.8-slim

ENV PYTHONUNBUFFERED1=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app
ENV PYTHONPATH /app
#edit => it cause error
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip --no-cache && \
    pip install -r requirements.txt --no-cache && \
    rm /app/requirements.txt

COPY scripts /app/scripts
EXPOSE 5010
COPY app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001"]
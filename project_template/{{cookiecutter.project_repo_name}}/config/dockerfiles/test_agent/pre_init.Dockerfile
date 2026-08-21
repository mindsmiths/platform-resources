FROM python:3.10-bookworm

RUN pip install playwright==1.45.0 && playwright install --with-deps

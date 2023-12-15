FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN pip install -U pip setuptools wheel && \
    pip install -U spacy && \
    python -m spacy download en_core_web_sm
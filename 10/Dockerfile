FROM python:slim

WORKDIR /script

RUN groupadd -r teste && useradd -r -g teste teste && \
    mkdir -p /home/teste && \
    chown -R teste:teste /home/teste

COPY --chown=teste:teste --chmod=744 script.py .

USER teste

EXPOSE 8000

CMD ["python", "script.py"]

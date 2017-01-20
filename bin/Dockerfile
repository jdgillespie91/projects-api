FROM python:latest

COPY bin/entrypoint.sh /workspace/bin/entrypoint.sh
COPY projects /workspace/projects
COPY setup.py /workspace/setup.py
COPY setup.cfg /workspace/setup.cfg

WORKDIR /workspace

ENTRYPOINT ["/workspace/bin/entrypoint.sh"]

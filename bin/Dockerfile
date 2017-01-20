FROM python:latest

COPY bin/entrypoint.sh /workspace/bin/entrypoint.sh
COPY projects /workspace/projects
COPY setup.py /workspace/setup.py
COPY setup.cfg /workspace/setup.cfg

WORKDIR /workspace

RUN pip install --upgrade pip setuptools wheel
RUN python setup.py bdist_wheel
RUN pip install dist/*

ENTRYPOINT ["/workspace/bin/entrypoint.sh"]

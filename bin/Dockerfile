FROM python:slim

WORKDIR /workspace

COPY projects /workspace/projects
COPY setup.py /workspace/setup.py
COPY setup.cfg /workspace/setup.cfg

RUN pip install --upgrade pip setuptools wheel
RUN python setup.py bdist_wheel
RUN pip install dist/*

RUN rm -r /workspace

COPY bin/entrypoint /entrypoint
ENTRYPOINT ["/entrypoint"]

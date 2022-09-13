ARG python=python:3.9-alpine

FROM ${python} as build
WORKDIR /code

COPY requirements.txt .
RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

RUN pip install --no-cache-dir --upgrade  -r requirements.txt


FROM ${python}
COPY --from=build /venv /venv
WORKDIR /code
ENV PATH=/venv/bin:$PATH

COPY . .

CMD ["python3", "main.py"]

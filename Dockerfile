FROM python:3.12-slim
LABEL authors="norbert"

WORKDIR /margo_calc

COPY margo_calc/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./margo_calc /margo_calc

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
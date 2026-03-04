#Builder
FROM python:3.13.5-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/deps -r requirements.txt

#Distroless
FROM gcr.io/distroless/python3-debian13:nonroot
WORKDIR /app
COPY --from=builder /deps /deps
ENV PYTHONPATH=/deps
COPY citations_haddock_users.py /app/citations_haddock_users.py
ENV PYTHONUNBUFFERED=1
EXPOSE 5000
CMD ["/app/citations_haddock_users.py"]
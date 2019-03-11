FROM python:3.6.7-alpine
WORKDIR /app
COPY requirements.txt ./
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk update && \
    apk add --no-cache --virtual .build-deps \
    gcc \
    g++ \
    make \
    libffi-dev \
    openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps && \
    rm -rf /etc/apk
COPY . .
# RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
EXPOSE 5000

# rm -rf /var/cache/apk/* && \
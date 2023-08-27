FROM alpine:3.7
WORKDIR /app
RUN mkdir -p /app/eng \
  && apk update \
  && apk add --no-cache git build-base g++ perl perl-dev perl-time-hires perl-compress-raw-zlib readline readline-dev ncurses-libs ncurses-terminfo-base ncurses-dev python2 curl curl-dev nano dos2unix mysql-client bind-tools \
  && git clone https://github.com/openkore/openkore.git /app/eng \
  && ln -s /usr/lib/libncurses.so /usr/lib/libtermcap.so \
  && ln -s /usr/lib/libncurses.a /usr/lib/libtermcap.a \
  && cd /app/eng \
  && make
COPY ./start.sh /app/start.sh
COPY ./data/tables/ /app/eng/tables/
RUN chmod +x /app/start.sh
ENTRYPOINT ["sh", "./start.sh"]

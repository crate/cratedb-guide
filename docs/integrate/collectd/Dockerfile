FROM docker.io/debian:13-slim

# Configure system environment.
ENV DEBIAN_FRONTEND=noninteractive

# Install collectd.
RUN apt update --yes && apt install --yes collectd

# Run collectd in foreground.
ENTRYPOINT ["collectd", "-f"]

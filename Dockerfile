ARG SRC_TAG=latest
FROM netboxcommunity/netbox:${SRC_TAG}

LABEL org.opencontainers.image.title="Custom NetBox with plugins" \
      org.opencontainers.image.description="Custom (unofficial/community) build of netbox-docker with all \"certified\/\"compatible\" plugins installed" \
      org.opencontainers.image.source="https://github.com/danielskowronski/custom-netbox-docker-with-plugins" \
      org.opencontainers.image.url="https://github.com/danielskowronski/custom-netbox-docker-with-plugins" \
      org.opencontainers.image.documentation="https://github.com/danielskowronski/custom-netbox-docker-with-plugins/blob/main/README.md" \
      org.opencontainers.image.base.name="netboxcommunity/netbox:${SRC_TAG}"

COPY requirements.txt /requirements.txt
COPY tools/inside-report.sh /report.sh
COPY plugins.py /etc/netbox/config/plugins.py

RUN mkdir -p /opt/netbox/netbox/media/netbox-attachments && \
  chown $(stat -c '%U' /opt/netbox/netbox/media):$(stat -c '%G' /opt/netbox/netbox/media) /opt/netbox/netbox/media/netbox-attachments

RUN /usr/local/bin/uv pip install \
  --python /opt/netbox/venv/bin/python \
  --no-cache-dir \
  -r /requirements.txt

RUN SECRET_KEY=secret-key-change-me-fffffffffffffffffffffffffffff /opt/netbox/venv/bin/python3 /opt/netbox/netbox/manage.py collectstatic --no-input

RUN echo '' > /etc/netbox/config/plugins.py

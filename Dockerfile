FROM netboxcommunity/netbox:latest

COPY requirements.txt /requirements.txt
COPY tools/inside-report.sh /report.sh

RUN mkdir -p /opt/netbox/netbox/media/netbox-attachments && \
  chown unit /opt/netbox/netbox/media/netbox-attachments

RUN /usr/local/bin/uv pip install \
  --python /opt/netbox/venv/bin/python \
  --no-cache-dir \
  -r /requirements.txt

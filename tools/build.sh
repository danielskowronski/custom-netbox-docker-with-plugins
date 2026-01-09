#!/bin/bash

SRC_REPO="netbox-community/netbox"
DST_IMG="ghcr.io/danielskowronski/custom-netbox-docker-with-plugins"

SRC_TAG=$1
if [ -z "$SRC_TAG" ]; then
  SRC_TAG=`curl -s https://api.github.com/repos/${SRC_REPO}/releases/latest | jq -r .tag_name`
fi

DST_SUFIX=$2
if [ -z "$DST_SUFIX" ]; then
  DST_SUFIX=`date -u +"%Y%m%d%H%M%S"`
fi
DST_TAG="${DST_IMG}:${SRC_TAG}-${DST_SUFIX}"

echo "Building image ${DST_TAG} from source repo ${SRC_REPO}:${SRC_TAG}..."

docker buildx build --platform linux/amd64,linux/arm64 -t ${DST_TAG} --push ..

docker run --rm ${DST_TAG} /report.sh > "report-${SRC_TAG}-${DST_SUFIX}.txt"
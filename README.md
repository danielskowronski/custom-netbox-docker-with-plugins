# custom-netbox-docker-with-plugins

**Custom (unofficial/community) build of netbox-docker with all "certified"/"compatible" plugins installed**

Docker image with automatic build pipelines to solve very old issue with Netbox - terrible plugins system, which is based on Python packages and thefore not very compatible with containers, especially on Kubernetes. 

[netboxlabs.com/plugins](https://netboxlabs.com/plugins/) is taken as base list of plugins to be installed

## Mechanism v1

- build process is based on upstream versioning of Netbox Docker image - each version will trigger new build here
- plugins are installed on top of that image - *intentionally* using unpinned latest version of PyPI packages; this can lead to one of three scenarios:
  - version works - happy path
  - plugin does not support latest Netbox version yet - intentionally kept that way, since Netbox version is prioritized and older releases are available; nothing breaks if plugin is not enabled in `PLUGINS` configuration
  - plugin supports latest Netbox version but it's broken - same as above, but some improvements will be provided in v2 of build mechanism 

## Plugins and Dockerfile

[`requirements.txt`](./requirements.txt) reflects state of [netboxlabs.com/plugins](https://netboxlabs.com/plugins/). It's also source of truth for hard plugin exclusions (mainly unclear status and lack of v4.x compatibility)

[`Dockerfile`](./Dockerfile) installs plugins from `requirements.txt` and implements minimum set of extra changes required by some plugins (e.g. extra directory to be created).

## Examples

### docker-compose

```bash
cd example/docker-compose
docker compose up -d --build
```

[`example/docker-compose`](./example/docker-compose) subdirectory provides:

- minimal docker-compose which runs Redis, Postgres and Netbox based on freshly built Dockerfile
- **insecure** minimum passwords and config in [`netbox.env`](./example/netbox.env)
- minimal plugin configuration in [`plugins.py`](./example/plugins.py) intended to start all plugins that are:
  - compatible with latest version of Netbox (v4.5)
  - self-contained, i.e. not requiring external systems to work
- links to documentations of plugin configuration options in `plugins.py`

After waiting for DB to initialize, visit [http://localhost:8000](http://localhost:8000) and log in with `admin:admin`.


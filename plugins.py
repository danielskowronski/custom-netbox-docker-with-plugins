# this file is only for initial collectstatic during build

PLUGINS = [
  #"validity", # does not support v4.5.0 yet
  #"netbox_routing", # does not support v4.5.0 yet - crash
  "netbox_prometheus_sd",
  #"netbox_otp_plugin", # does not support v4.5.0 yet
  #"netbox_napalm_plugin", # disabled by default as it requires extra configuration
  "netbox_lists",
  "netbox_lifecycle",
  "netbox_kea",
  #"netbox_inventory", # does not support v4.5.0 yet - crash
  "netbox_interface_synchronization",
  "netbox_documents",
  "netbox_data_flows",
  "netbox_contract",
  #"netbox_config_diff", # disabled by default as it requires extra configuration
  "netbox_attachments",
  #"nb_service", # does not support v4.5.0 yet
  #"nb_risk", # does not support v4.5.0 yet
  "netbox_topology_views",
  #"slurpit_netbox", # disabled by default as it requires extra configuration
  #"netbox_secrets", # does not support v4.5.0 yet
  "netbox_reorder_rack",
  "netbox_qrcode",
  #"ipfabric_netbox", # disabled by default as it requires extra configuration
  "netbox_floorplan",
  "netbox_dns",
  "netbox_bgp",
]

PLUGINS_CONFIG = { }

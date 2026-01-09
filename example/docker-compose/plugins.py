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

PLUGINS_CONFIG = {
  # https://validity.readthedocs.io/en/latest/installation/plugin_settings/
  "validity": { 
    
  },
  
  # https://github.com/k1nky/netbox-otp-plugin
  "netbox_otp_plugin": {
    "otp_required": False,
    "issuer": 'MyOrgNetbox'
  },
  
  # https://github.com/netbox-community/netbox-napalm-plugin?tab=readme-ov-file#configure-plugin
  "netbox_napalm_plugin": {
    "NAPALM_USERNAME": "xxx",
    "NAPALM_PASSWORD": "yyy",
  },
  
  # https://github.com/devon-mar/netbox-lists?tab=readme-ov-file#plugin-config
  "netbox_lists": {
    
  },
  
  # https://github.com/DanSheps/netbox-lifecycle?tab=readme-ov-file#configuration
  "netbox_lifecycle": {
    "lifecycle_card_position": "right_page",
    "contract_card_position": "right_page",
  },
  
  # https://github.com/ArnesSI/netbox-inventory?tab=readme-ov-file#settings
  "netbox_inventory": {
    
  },
  
  # https://github.com/NetTech2001/netbox-interface-synchronization?tab=readme-ov-file#plugin-settings
  "netbox_interface_synchronization": {
    
  },
  
  # https://github.com/jasonyates/netbox-documents?tab=readme-ov-file#enable-the-plugin
  "netbox_documents": {
    
  },
  
  # https://alef-burzmali.github.io/netbox-data-flows/installation-configuration/#configuration
  "netbox_data_flows": {
    
  },
  
  # https://github.com/mlebreuil/netbox-contract?tab=readme-ov-file#customize-the-plugin
  "netbox_contract": {
    
  },
  
  # https://github.com/miaow2/netbox-config-diff?tab=readme-ov-file#installing
  "netbox_config_diff": {
    
  },
  
  # https://github.com/Kani999/netbox-attachments?tab=readme-ov-file#plugin-options
  "netbox_attachments": {
    
  },
  
  # https://github.com/renatoalmeidaoliveira/nbservice?tab=readme-ov-file#configuration
  "nb_service": {
    "top_level_menu": True,
  },
  
  # https://github.com/renatoalmeidaoliveira/nbrisk?tab=readme-ov-file#configuration
  "nb_risk": {
    
  },
  
  # https://github.com/netbox-community/netbox-topology-views?tab=readme-ov-file#individual-options
  "netbox_topology_views": {
    "allow_coordinates_saving": True,
  },
  
  # https://github.com/Onemind-Services-LLC/netbox-secrets?tab=readme-ov-file#configuration
  "netbox_secrets": {
    
  },
  
  # https://github.com/netbox-community/netbox-qrcode/blob/master/docs/README_Subpages/README_Configuration.md
  "netbox_qrcode": {
    
  },
  
  # https://github.com/netbox-community/netbox-bgp?tab=readme-ov-file#configuration
  "netbox_bgp": {
    
  },
}
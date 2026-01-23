#!/usr/bin/env python3
"""
Generate navbar.js from Hugo's menu configuration
"""

import json
import yaml
import re
from pathlib import Path

# Read config.yaml to get menu items
config_path = Path("config.yaml")
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

# Extract menu items
menu_items = []
if 'menu' in config and 'main' in config['menu']:
    for item in config['menu']['main']:
        menu_items.append({
            'name': item.get('name', ''),
            'url': item.get('url', ''),
            'title': item.get('name', ''),
            'external': item.get('url', '').startswith('http')
        })

# Read the template
template_path = Path("assets/js/navbar.tmpl.txt")
with open(template_path, 'r') as f:
    template = f.read()

# Build the menu items JavaScript array with proper formatting
menu_json_items = []
for item in menu_items:
    menu_json_items.append(f"""    {{
      name: {json.dumps(item['name'])},
      url: {json.dumps(item['url'])},
      title: {json.dumps(item['title'])},
      external: {json.dumps(item['external'])}
    }}""")

menu_items_js = ",\n".join(menu_json_items)

# Replace the Hugo template section with the actual menu items
# Find everything between {{- range .Site.Menus.main }} and {{- end }}
pattern = r'\{\{-\s*range\s+\.Site\.Menus\.main\s*\}\}.*?\{\{-\s*end\s*\}\}'
replacement = menu_items_js

navbar_js = re.sub(pattern, replacement, template, flags=re.DOTALL)

# Create output directory
output_dir = Path("public/navbar")
output_dir.mkdir(parents=True, exist_ok=True)

# Write the output
output_path = output_dir / "navbar.js"
with open(output_path, 'w') as f:
    f.write(navbar_js)

print(f"Generated {output_path}")

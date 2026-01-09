#!/bin/bash
while read -r pkg; do
  echo "$pkg" | grep -q '^[a-zA-Z]' 2>/dev/null 
  if [[ $? -ne 0 ]]; then
    continue
  fi
 /usr/local/bin/uv pip show "$pkg" 2>/dev/null | grep ^Version: | sed "s/^Version: /$pkg==/"
done < /requirements.txt
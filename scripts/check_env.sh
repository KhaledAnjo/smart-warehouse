#!/usr/bin/env bash
# check_env.sh - check that the tools this project needs are installed

echo "=== Environment check ==="
echo "User: $(whoami)"
echo "Date: $(date)"

for tool in git python3 curl docker ; do
  if command -v "$tool" > /dev/null; then
    echo "[OK]      $tool: $($tool --version | head -n 1)"
  else
    echo "[MISSING] $tool"
  fi
done

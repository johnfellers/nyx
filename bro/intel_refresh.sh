#!/bin/bash

# add this to the crontbab:
# */5 * * * * [script_location]/intel_refresh.sh > /var/log/intel.log

cd [script_location]
rm CRITs.intel*
wget -q http://[repository_web_server]/CRITs.intel

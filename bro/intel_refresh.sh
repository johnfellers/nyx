#!/bin/bash

# add this to the crontbab:
<<<<<<< HEAD
# */5 * * * * [script_location]/intel_refresh.sh > /var/log/intel.log

cd [script_location]
rm CRITs.intel*
wget -q http://[repository_web_server]/CRITs.intel
=======
# */5 * * * * /opt/bro/intel/intel_refresh.sh > /var/log/intel.log

cd /opt/bro/intel/
rm CRITs.intel*
wget -q http://192.168.11.38/CRITs.intel
>>>>>>> upstream/master

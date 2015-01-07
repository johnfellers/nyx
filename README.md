nyx
===

Threat Intelligence artifact distribution

The goal of this project is to facilitate distribution of Threat Intelligence artifacts to defensive systems and to enhance the value derrived from both open source and commercial tools.

The technologies currently coded for are: 
- IBM QRadar
- Palo Alto Networks
- CRITs
- BRO IDS
- URL blocklist for a web filter

To get startef with this, fill out the configuration file with the appropriate values and run nyx.conf. If you don't have some of the technologies in your environment, remove the configuration section.

Make sure that the user running this has the rights to the configuration file, as well as the output files. When implementing this in production, it might be worthwile to place the conf files in a /etc/nyx-like folder for more stability and run the nyx.py script on a regular basis using crontab.

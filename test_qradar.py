import json
from common_methods import read_configs
from qradar import *

test_ips=["54.243.185.88","192.187.114.250","217.23.7.169","195.211.155.251","91.207.6.138","60.173.11.248"]
test_domains=["isolectra.com.sg","hosted-by.ihc.ru","50-87-149-90.unifiedlayer.com","sdaexpress24.net","wa4.rzone.de","http.apache1.cp247.net","box751.bluehost.com"]
test_emails=['riojasm66@yahoo.com','hdclive@live.com','terauau@gmail.com','jabu_moleketi@yahoo.com','soeungkheng34@yahoo.com','desk433@yahoo.com','caf432@ig.com.br','samanthakipkalya24@yahoo.in','cpt.jane@yahoo.com.ph','edwardbuma02@hotmail.com','mrsgracetoddclark@yahoo.co.jp','grace1todd1@daum.net','mrmaxofori1@outlook.fr','mrmax.ofori@aol.fr','barakahumao1@yahoo.es','peter.kofi1@rediffmail.com','guaranteloans@aol.com','mallam.umaru@yandex.com','consty22@gmail.com','madii002@terra.com','madiii00@aol.fr','mr-davieswalkermr-prom01@live.com','markjerryloans02@hotmail.com','drgilbertblair_unionbkfundsplc@hotmail.co.uk','tom_crist_donation@rogers.com','kasimaiga001@gmail.com']
test_hashes=['d84a99e6642cf6c75a54451c46d30727','22eb1302206a3fc956a01e1d77a2cacf','8f849e680991f1c8826ce009ebaf2531','474dc1962dcc0587abca93e319331527','59293db92c3e22ffd2220cde919192ea','9c81422f7454292c5982c2be43eaa577','2e430f5f9d0bce0b3338207da59a10ce','a8f953d728ebac222ef1e60ff95f1481','f7f9d2754416a4f3319bf9e0d6bd9dee','a5474ba2dd544ca20f6bca7d1b4b32ce','eefe9d8c61eff800ba25e83d23911a9a','16dc2e406808432ff51b69e1f7838376','f35b03abb7cf67d563655a3c12070d86','c8aea949204af57a85369feffc85f43e','dd3fb3333059f4e22b2dd31cd1212580']
test_userids=['user10','user11','user12','user13','user14','user15','user16','user17','user18','user19','user20','user21','user22','user23',]
qsettings=read_configs('nyx.conf')['qradar']

# add the ips to known indexes
for ip in test_ips:
    add_to_reference_set(qsettings['high_reference_sets']['Address - ipv4-addr'],ip,'nyx_qradar_test',qsettings)
    add_to_reference_set(qsettings['medium_reference_sets']['Address - ipv4-addr'],ip,'nyx_qradar_test',qsettings)

# add domains
for domain in test_domains:
    add_to_reference_set(qsettings['high_reference_sets']['A'],domain,'nyx_qradar_test',qsettings)
    add_to_reference_set(qsettings['medium_reference_sets']['A'],domain,'nyx_qradar_test',qsettings)

# add hashes
for md5 in test_hashes:
    add_to_reference_set(qsettings['high_reference_sets']['md5'],md5,'nyx_qradar_test',qsettings)
    add_to_reference_set(qsettings['medium_reference_sets']['md5'],md5,'nyx_qradar_test',qsettings)

# add emails
for email in test_emails:
    add_to_reference_set(qsettings['high_reference_sets']['email'],email,'nyx_qradar_test',qsettings)
    add_to_reference_set(qsettings['medium_reference_sets']['email'],email,'nyx_qradar_test',qsettings)
    
# add user ids:
for userid in test_userids:
    add_to_reference_set(qsettings['high_reference_sets']['userid'],userid,'nyx_qradar_test',qsettings)
    
# listing reference_sets
for qset in qsettings['medium_reference_sets'].values()+qsettings['high_reference_sets'].values():
    print qset,len(list_reference_set(qset,qsettings))
"""
# remove the ips
for ip in test_ips:
    remove_from_reference_set(qsettings['high_reference_sets']['Address - ipv4-addr'],ip,qsettings)
    remove_from_reference_set(qsettings['medium_reference_sets']['Address - ipv4-addr'],ip,qsettings)

# remove domains
for domain in test_domains:
    remove_from_reference_set(qsettings['high_reference_sets']['A'],domain,qsettings)
    remove_from_reference_set(qsettings['medium_reference_sets']['A'],domain,qsettings)

# remove hashes
for md5 in test_hashes:
    remove_from_reference_set(qsettings['high_reference_sets']['md5'],md5,qsettings)
    remove_from_reference_set(qsettings['medium_reference_sets']['md5'],md5,qsettings)
    
# remove emails
for email in test_emails:
    remove_from_reference_set(qsettings['high_reference_sets']['email'],email,qsettings)
    remove_from_reference_set(qsettings['medium_reference_sets']['email'],email,qsettings)

# remove user ids:
for userid in test_userids:
    remove_from_reference_set(qsettings['high_reference_sets']['userid'],userid,qsettings)
    

# listing reference_sets
for qset in qsettings['medium_reference_sets'].values()+qsettings['high_reference_sets'].values():
    print qset, len(list_reference_set(qset,qsettings))
"""
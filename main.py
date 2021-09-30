import feedparser
from  time import sleep 
from domain import Domain, SubDomain

#
# put a list of URL in the urls.txt file and run:
# awk -F'/' '{n=split($3, a, "."); print a[n-1]"."a[n] }' urls.txt | sort | uniq | sort > domini.txt
#

URL= "https://crt.sh/atom?q=%s"

hnd = open('domini.txt', 'r')
domains = hnd.readlines()
hnd.close()

for domain in domains: 
    domobj = Domain(domain)
    
    feed = feedparser.parse( URL % domain )
    feed_entries = feed.entries
    for entry in feed.entries:
    
        buf = entry.summary.split("<br") 
        subdominio = ''
        for b in buf[0].split('\n'):
            subdominio = subdominio.strip() + " " + b

        domobj.append_subdomain(subdominio)
        subdom = domobj.get_subdomain(subdominio)
        subdom.published(entry.published) # Unicode string
        subdom.updated(entry.updated) # Time object

    domobj.print_subdomains()
    sleep(2)

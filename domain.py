
class SubDomain:
    def __init__(self, subdomain):
        self.name = subdomain
        self.cert_updated = []
        self.cert_published_at = []

    def updated(self, t):
        self.cert_updated.append(t)

    def published(self, t):
        self.cert_published_at.append(t)

    def __str__(self):
        print ("SubDomain: %s" % self.name)
        print ("published_at")
        print (self.cert_published_at)
        print ("updated")
        print (self.cert_updated)

    def sort(self):
        self.cert_updated.sort(reverse=True)
        self.cert_published_at.sort(reverse=True)
    
    def get_recent(self):
        print("%s %s %s" % (self.cert_published_at[0], self.cert_updated[0], self.name) )
        
        
class Domain: 
    def __init__(self, name):
        self.name = name.strip()
        self.subdomains = {}       

    def append_subdomain(self, sname):
        name = sname.strip()
        if not name in self.subdomains.keys():
            sub = SubDomain(name)
            self.subdomains[name]= sub
        return self.subdomains[name]
    
    def get_subdomain(self, name):
        n = name.strip()
        return self.subdomains[n]

    def print_subdomains(self):
        print ("-----------------------------------------------")
        print ("main: " + self.name)
        for k,v in self.subdomains.items():
            subobj = self.get_subdomain(k)
            subobj.sort()
            subobj.get_recent()


releasever = "6"
filerepo = "/etc/yum.repos.d/nginx.repo"
nginxrepo = """[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/"""+releasever+"""/$basearch/
gpgcheck=0
enabled=1"""

def file_exists(filepath):
  #{
  import os.path
  return os.path.exists(filepath)
  #}
  
def file_create (filepath, connten):
  #{
  target = open (filepath, 'a')
  target.write(connten)
  target.close()
  #}
  
if(file_exists(filerepo)):
  #{
  file_create(filerepo, nginxrepo)
  print("Create " + filerepo)
  #} 




nginxrepo = """[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=0
enabled=1"""

def file_exists(filepath):
  #{
  import os.path
  return os.path.exists(filepath)
  #}
  
def file_create (filepath, connten):
  #{
  print(filepath, connten)
  #}
  
if(file_exists("/etc/yum.repos.d/nginx.repo")):
  #{
  file_create("/etc/yum.repos.d/nginx.repo", nginxrepo)
  #}
else:
  print("no existe")

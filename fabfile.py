from fabric.api import *

# Hosts you wish to deploy to
env.hosts = ['sandy@localhost:22']

def pushpull():
    local('git push') # run command on local env
    run('cd /var/www/polls/; git pull') #run command on remote env

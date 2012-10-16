from fabric.api import *

# Hosts you wish to deploy to
env.hosts = ['deploy@198.61.213.160:22']

def pushpull():
    local('git push') # run command on local env
    run('cd /var/www/polls/; git pull') #run command on remote env

def restartservices():
    # remotely, restart uWSGI
    run('sudo service mysite-uwsgi restart')

    # remotely, reload NGINX
    run('sudo nginx -s reload')


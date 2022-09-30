# Redo the task #0 but by using Puppet:

excec { 'command':
    command => "apt-get -y update;
    apt-get -y install nginx;
    mkdir -p /data/web_static/;
    mkdir -p /data/web_static/shared/;
    mkdir -p /data/web_static/releases/test/;
    echo Holberton School" > /data/web_static/releases/test/index.html;
    ln -sf /data/web_static/releases/test/ /data/web_static/current;
    chown -R ubuntu:ubuntu /data/;
    HBNB_STATIC='\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}';
    sed -i '29i\ $HBNB_STATIC' /etc/nginx/sites-available/default;
    service nginx restart;",
    provider => shell,
}
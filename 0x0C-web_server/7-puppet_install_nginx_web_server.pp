# install and config nginx server
 
exec { 'configure_nginx':
  command => 'apt-get -y update && apt-get -y install nginx && echo "Hello World!" > /var/www/html/index.html && echo "server {\n    listen 80;\n    listen [::]:80 default_server;\n    root   /etc/nginx/html;\n    index  index.html;\n    location /redirect_me {\n        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n    }\n}" > /etc/nginx/sites-available/default && service nginx start',
}


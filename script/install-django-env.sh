# Pacotes necessarios 
sudo apt-get install libldap2-dev libsasl2-dev libssl-dev python-virtualenv python2.6 python2.6-dev
virtualenv -p /usr/bin/python2.6 --no-site-packages --distribute ~/VirtualEnvs/Mocambos_Portal
source ~/VirtualEnvs/Mocambos_Portal/bin/activate
pip install -r requirements.txt

# # Pacotes necessarios para django-filer
# sudo apt-get install libfreetype6-dev liblcms1-dev libjpeg8-dev
# pip install django-filer

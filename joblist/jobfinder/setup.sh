# Update system
# sudo apt update && sudo apt upgrade -y
# Add deadsnakes PPA for Python 3.11
# sudo add-apt-repository ppa:deadsnakes/ppa -y
# sudo apt update 
sudo apt install python3
sudo apt install python3-pip
pip install virtualenv
python3 -m venv jobfinder
source jobfinder/bin/activate
pip install django
pip install -r requirements.txt
# python3 call_socket/tests.py
# python3 manage.py runserver 0.0.0.0:8001

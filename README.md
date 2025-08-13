sudo apt install openmpi-bin libopenmpi-dev
sudo apt update
sudo apt install -y rabbitmq-server    # pulls Erlang too
sudo systemctl enable --now rabbitmq-server
sudo rabbitmq-plugins enable rabbitmq_management
sudo systemctl restart rabbitmq-server
sudo systemctl status rabbitmq-server
ss -lntp | grep -E '5672|15672'
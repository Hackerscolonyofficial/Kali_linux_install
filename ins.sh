termux-setup-storage -y
cd
apt update ; apt upgrade -y
pkg install wget -y
wget -O install-nethunter-termux https://offs.ec/2MceZWr
bash install-nethunter-termux

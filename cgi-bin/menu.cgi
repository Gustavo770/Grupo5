#!/usr/bin/python
#-*- coding: utf8 -*-
var=raw_input()

import os

acao=var.split("=")[0]
print("content-type: text/html")
print("")
if acao == "d_i":
    os.system("sudo /usr/lib/cgi-bin/script.sh bind9 start")
    print("<h1>Iniciando!</h1>")
elif acao == "d_p":
    os.system("sudo /usr/lib/cgi-bin/script.sh bind9 stop")
    print("<h1>parando!</h1>")
elif acao == "d_r":
    os.system("sudo /usr/lib/cgi-bin/script.sh bind9 restart")
    print("<h1>Reiniciando!</h1>")
elif acao == "d_s":
    os.system("sudo /usr/lib/cgi-bin/status.sh bind9 status | grep Active:")
    status = open("/var/www/html/cgi-bin/status.txt", "r")
    html=status.read()
    status.close()
    print(html)
elif acao == "f_i":
    os.system("sudo /usr/lib/cgi-bin/regra.sh")
    print("<h1>Iniciado!</h1>")
elif acao == "f_p":
    os.system("sudo /usr/lib/cgi-bin/panico.sh")
    print("<h1>Parado!</h1>")
elif acao == "f_r":
    os.system("sudo /usr/lib/cgi-bin/regra.sh")
    print("<h1>Reiniciado!</h1>")
elif acao == "f_s":
    os.system("sudo /var/www/html/cgi-bin/firewall.sh")
    status = open("/var/www/html/cgi-bin/firewall.txt", "r")
    html=status.read()
    status.close()
    print(html)
elif acao == "n_i":
    os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 start")
    print("<h1>Iniciando!</h1>")
elif acao == "n_p":
    os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 stop")
    print("<h1>parando!</h1>")
elif acao == "n_r":
    os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
    print("<h1>Reiniciando!</h1>")
elif acao == "n_s":
    os.system("sudo /usr/lib/cgi-bin/status.sh nagios3 status")
    status = open("/var/www/html/cgi-bin/status.txt", "r")
    html=status.read()
    status.close()
    print(html)

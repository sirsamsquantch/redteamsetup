#test
import os

os.system('sudo apt update')
os.system('sudo apt upgrade')

os.system('sudo apt install python3')
os.system('sudo apt install python3-pip')
os.system('pip3 install oletools')
os.system('pip3 install pycrypto')
os.system('pip3 install pwntools')
os.system('pip3 install volatility')

os.system('sudo apt install sublime-text')
os.system('sudo apt install tmux')
os.system('sudo apt install terminator')

toolDir = os.path.expanduser("~/Desktop/tools")
os.system('mkdir '+toolDir)

os.system('git clone https://github.com/trustedsec/ptf.git '+toolDir)

os.system('wget http://didierstevens.com/files/software/DidierStevensSuite.zip -P '+toolDir)
os.system('unzip '+toolDir+'/DidierStevensSuite.zip')
os.system('rm '+toolDir+'/DidierStevensSuite.zip')

os.system('git clone https://github.com/longld/peda.git ~/peda')
os.system('echo "source ~/peda/peda.py" >> ~/.gdbinit')

pftCustom = toolDir+'/ptf/custom_lists/samsquantch'

f = open('pftCustom', 'a')

modules = [
	'modules/exploitation/metasploit', 
	'modules/vulnerability-analysis/nmap',
	'modules/vulnerability-analysis/whatweb', 
	'modules/exploitation/nosqlmap', 
	'modules/exploitation/sqlmap', 
	'modules/intelligence-gathering/wafw00f', 
	'modules/intelligence-gathering/dnsrecon',
	'modules/reversing/binwalk',
	'modules/password-recovery/install_update_all'
	]

for module in modules:
	f.write(module+'/n')
f.close()

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

homeDir = os.path.expanduser("~/")
toolDir = os.path.expanduser(homeDir+"Desktop/tools")
os.system('mkdir '+toolDir)
os.system('mkdir '+toolDir+'/ptf')

os.system('git clone https://github.com/trustedsec/ptf.git '+toolDir+'/ptf')
os.system('git clone https://github.com/volatilityfoundation/volatility.git'+toolDir)
os.system('python3 '+toolDir+'/setup.py install')

os.system('wget http://didierstevens.com/files/software/DidierStevensSuite.zip -P '+toolDir)
os.system('unzip '+toolDir+'/DidierStevensSuite.zip')
os.system('rm '+toolDir+'/DidierStevensSuite.zip')
os.system('mv DidierStevensSuite '+toolDir)

os.system('git clone https://github.com/longld/peda.git '+homeDir+'peda')
os.system('echo "source '+homeDir+'peda/peda.py" >> '+homeDir+'.gdbinit')

pftCustom = toolDir+'/ptf/modules/custom_list/samsquantch'

f = open(pftCustom, 'a')

modules = [
	'modules/exploitation/metasploit', 
	'modules/vulnerability-analysis/nmap',
	'modules/vulnerability-analysis/whatweb', 
	'modules/exploitation/nosqlmap', 
	'modules/exploitation/sqlmap',
	'modules/exploitation/findsploit',
	'modules/intelligence-gathering/wafw00f', 
	'modules/intelligence-gathering/dnsrecon',
	'modules/reversing/binwalk',
	'modules/password-recovery/install_update_all'
	]

for module in modules:
	f.write(module+'\n')
f.close()

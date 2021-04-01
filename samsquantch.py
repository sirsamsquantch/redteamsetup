import os

toolDir = os.path.expanduser("~/Desktop/tools")

os.system('mkdir '+toolDir)
os.system('git clone https://github.com/trustedsec/ptf.git '+toolDir)
os.system('wget http://didierstevens.com/files/software/DidierStevensSuite.zip -P '+toolDir)
os.system('unzip '+toolDir+'/DidierStevensSuite.zip')
os.system('rm '+toolDir+'/DidierStevensSuite.zip')
os.system('pip3 install oletools')
os.system('pip3 install pycrypto')


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

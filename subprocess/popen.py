import subprocess
args = ['ping','-c', '10', 'www.baidu.com']
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
print(data)
lll;id;
llls;


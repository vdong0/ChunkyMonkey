import os
import time
os.system("ssh -i /home/rrobrien/rrobrien-keypair rrobrien@100.26.104.102 killall -9 java")
os.system("ssh -i /home/rrobrien/rrobrien-keypair rrobrien@54.209.66.61 killall -9 java")
os.system("ssh -i /home/rrobrien/rrobrien-keypair rrobrien@100.26.104.102 rm Master.class")
os.system("ssh -i /home/rrobrien/rrobrien-keypair rrobrien@54.209.66.61 rm Node.class")
os.system("scp -i /home/rrobrien/rrobrien-keypair Master.class rrobrien@100.26.104.102:/home/rrobrien")
os.system("scp -i /home/rrobrien/rrobrien-keypair Node.class rrobrien@54.209.66.61:/home/rrobrien")
n = os.fork()
if n > 0:
    
    os.system("ssh -i /home/rrobrien/rrobrien-keypair rrobrien@100.26.104.102 java -Djava.rmi.server.hostname=100.26.104.102 Master ")
else:
    time.sleep(2)
    os.system("ssh -i /home/rrobrien/rrobrien-keypair rrobrien@54.209.66.61 java Node 54.209.66.61 100.26.104.102")
    os.system("ssh -i /home/rrobrien/rrobrien-keypair rrobrien@54.209.66.61 1 test.txt 0")

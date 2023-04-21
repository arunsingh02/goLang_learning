ch_flag = False

def a():
    d = {
    'FailedToUpdateBroadcastDomainForPort':
        {'category': 'node', 'message': 'Error while updating broadcast domain for port %s on node "%s"'}
    }
    params = ('Arun', 'Ravi')
    print(d["FailedToUpdateBroadcastDomainForPort"]["message"]% params)
    print(d)

if ch_flag:
    def b():
        print('Arun')
else:
    def c():
        print('Vishal')


# a()

import shutil
from subprocess import PIPE, run, CalledProcessError, Popen

CSERVER_PATH = '/Users/arunsingh/Desktop/Dump'
VAR_TEMPFILE = '/Users/arunsingh/Desktop/Dump/sshcfg'
FILE = '/Users/arunsingh/Desktop/Dump/.mfa_enabled'


def test_old(method):
    if method == 'enable':
        shutil.copyfile(CSERVER_PATH + '/sshd_config', VAR_TEMPFILE)
        # cmd = 'Match User admin\nAuthenticationMethods "publickey,password" "publickey,keyboard-interactive"'
        cmd = 'Match User admin'
        # print(cmd)
        conf_file = CSERVER_PATH + '/sshd_config'
        #cmd_args = ['sed', 'KexAlgorithms/a %s'%(cmd),  conf_file]
        #cmd_args = ['sed', '/\[b\]/a %s'%(cmd), conf_file]
        cmd_args = 'sed "s/b/&/\n%s/" %s'%(cmd, conf_file)
        success = False
        try:
            process = Popen(cmd_args, shell=True, stdout=PIPE, stderr=PIPE)
            err, res = process.communicate()
            print('>>>> ', [err, res])
            print(cmd_args)
            #Popen(cmd, shell=True)
            #shutil.copyfile(VAR_TEMPFILE, CSERVER_PATH + '/sshd_config')
            success = True
        except CalledProcessError as e:
            print(e)
            print("DATA : ", e.output)
        print(success)
    elif method == 'disable':
        cmd = 'sed -e "/Match User admin/,+2d" < %s > %s' % (CSERVER_PATH + '/sshd_config', CSERVER_PATH + '/sshd_config')
        print(cmd)
        run(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        # shutil.move(VAR_TEMPFILE, CSERVER_PATH + '/sshd_config')


def test(method):
    conf_file = CSERVER_PATH + '/sshd_config'
    if method == 'enable':
        cmd = 'Match User admin\nAuthenticationMethods "publickey,password" "publickey,keyboard-interactive"\n'
        success = False
        try:
            with open(conf_file, 'a') as f:
                f.write(cmd)
            success = True
        except Execption as err:
            print(err)
    elif method == 'disable':
        with open(conf_file, "r") as read_file:
            with open(VAR_TEMPFILE, "w") as write_file:
                # iterate all lines from file
                for line in read_file:
                    # if text matches then don't write it
                    line = line.strip('\n')
                    if not ("Match User admin" in line or 'AuthenticationMethods' in line):
                        write_file.write('%s\n' % line)
        shutil.copyfile(VAR_TEMPFILE, conf_file)

import sys
args = sys.argv
test(args[1])

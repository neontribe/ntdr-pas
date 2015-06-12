#! /usr/bin/env python

# Find changelog vesion
# Arguments are directories to search; default is /var/www/latest
# No recursion.

import sys, os, json, shlex, subprocess, errno, getpass, socket

# TODO import this from ntdr_get_version.py
def get_version(name):
    full = os.path.join(name, 'changelog.txt')
    if os.path.isfile(full):
        with open(full, 'r') as f:
            first_line = f.readline()
        parts = first_line.split();
        return parts[1]
    return False


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

''' Ansible uploads the args as a file '''
args_file = sys.argv[1]
args_data = file(args_file).read()

arguments = shlex.split(args_data)
if not arguments: arguments = ['/var/www/latest']

drpath = arguments[0].rstrip("/")

dirname = os.path.join(drpath, 'sites/all/drush')
version = get_version(drpath)
basename = os.path.basename(drpath)
aliasname = version
aliaspath = os.path.join(dirname, aliasname + '.alias.drushrc.php')

cmd = "drush -r " + drpath +" sa @self --full --with-db"
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
response = proc.stdout.read()

lines = response.split(os.linesep)
for index in range(len(lines)):
    line = lines[index]
    if 'self' in line:
        line = line.replace('self', aliasname)
        lines[index] = line
    if 'root' in line:
        line = "  'root' => '" + os.path.realpath(drpath) + "',"
        lines[index] = line
lines.insert(1, "  'remote_user' => '" + getpass.getuser() + "',")
lines.insert(1, "  'remote_host' => '" + socket.gethostname() + "',")

mkdir_p(dirname)
if os.path.isfile(aliaspath):
    os.remove(aliaspath)
with open(aliaspath, 'w') as f:
    f.write('<?php' + os.linesep)
    f.write(os.linesep.join(lines))

data = {}
data['basename'] = basename
data['version'] = version
data['aliasname'] = version
data['cmd'] = cmd
data['aliaspath'] = aliaspath
print json.dumps(data)
sys.exit(0)

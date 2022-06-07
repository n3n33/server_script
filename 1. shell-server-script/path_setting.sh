#!/usr/bin/env bash

files_name=$1

createPath() {
cat >>/etc/profile.d/${files_name} <<EOF

export TEST_HOME=/home

PATH=$PATH:$TEST_HOME

EOF
}

createPath

chmod +x /etc/profile.d/${files_name}

source /etc/profile.d/${files_name}

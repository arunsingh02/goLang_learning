#!/usr/bin/bash
CSERVER_PATH=/Users/arunsingh/Desktop/Dump
VAR_TEMPFILE=/Users/arunsingh/Desktop/Dump/sshcfg
FILE=/Users/arunsingh/Desktop/Dump/.mfa_enabled

if [ "$1" = enable ]
then
	if [ -f "$FILE" ]; then
    echo "$FILE already exists and MFA is already enabled"
    else
    sed '$ a\
        Match User admin \
        AuthenticationMethods \"publickey,password\" \"publickey,keyboard-interactive\" \
        ' $CSERVER_PATH/sshd_config > ${VAR_TEMPFILE}
        mv ${VAR_TEMPFILE} $CSERVER_PATH/sshd_config
   	# touch .mfa_enabled 
	# systemctl restart ssh
	echo "MFA enabled Successfully"
fi

elif [ "$1" = disable ]
then
	if [ -f "$FILE" ]; then
  	rm -i /Users/arunsingh/Desktop/Dump/.mfa_enabled 
	sed -e '/Match User \<admin\>/,+2d' $CSERVER_PATH/sshd_config > ${VAR_TEMPFILE}
        mv ${VAR_TEMPFILE} $CSERVER_PATH/sshd_config
	# systemctl restart ssh
	echo "MFA disabled Successfully"	
	else
	echo "$FILE does not exist and MFA not enabled yet" 
	fi
fi
	

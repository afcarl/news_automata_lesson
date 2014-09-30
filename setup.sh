# sets up pip on a non-privileged user account (i.e. w/o sudo)

curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py --user

if [ ! -f ~/.bash_profile ]; then
    touch ~/.bash_profile
fi

echo "PATH=\$PATH:~/Library/Python/2.7/bin" >> ~/.bash_profile

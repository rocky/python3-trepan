#!/bin/bash
PYTHON_VERSION=3.11.8

# FIXME put some of the below in a common routine
function checkout_version {
    local repo=$1
    version=${2:-master}
    echo Checking out $version on $repo ...
    (cd ../$repo && git checkout $version && pyenv local $PYTHON_VERSION) && \
	git pull
    return $?
}

export PATH=$HOME/.pyenv/bin/pyenv:$PATH
owd=$(pwd)
bs=${BASH_SOURCE[0]}
mydir=$(dirname $bs)
fulldir=$(readlink -f $mydir)
cd $mydir
(cd ../../python-uncompyle6 && ./admin-tools/setup-master.sh)
cd $fulldir/..
(cd $fulldir/.. && \
     checkout_version python-spark master && \
     checkout_version pycolumnize && \
     checkout_version python-xdis && \
     checkout_version python-filecache && \
     checkout_version python-uncompyle6 \
)

rm -v */.python-version || true

git checkout master && pyenv local $PYTHON_VERSION && git pull

cd $owd

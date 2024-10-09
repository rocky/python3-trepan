#!/bin/bash
# Check out master branch and dependent development master branches
bs=${BASH_SOURCE[0]}
if [[ $0 == $bs ]] ; then
    echo "This script should be *sourced* rather than run directly through bash"
    exit 1
fi

PYTHON_VERSION=3.12

mydir=$(dirname $bs)
trepan3k_owd=$(pwd)
cd $mydir
. ./checkout_common.sh
fulldir=$(readlink -f $mydir)
(cd $fulldir/.. && \
     setup_version python-uncompyle6 master && \
     setup_version python-xdis master && \
     setup_version python-filecache master && \
     setup_version shell-term-background master && \
     setup_version pytracer master && \
     setup_version pycolumnize master \
)

checkout_finish master

#!/bin/bash -x

# Copyright (c) 2013 Intel Corporation. All rights reserved.
# Use of this source code is governed by a LGPL v2.1 license that can be
# found in the LICENSE file in the db directory.
# Author : Ewan Le Bideau-Canevet


FILE=$1
UNWANTED="No decoder available"
COMMAND="gst-play-1.0 /$HOME/$FILE"

tmplog=$(mktemp --tmpdir=/tmp multimedia-XXXXXX.log)
trap "rm -f $tmplog" STOP INT QUIT EXIT
echo $COMMAND
$COMMAND &>$tmplog &
pid=$!
(sleep 5; [ -e /proc/$pid ] && kill $pid;) &
while [ -e /proc/$pid ]; do
	sleep 1
	if grep "$UNWANTED" $tmplog ; then
		kill $pid
		sleep 1
		[ -e /proc/$pid ] && kill -9 $pid
		exit 1
	fi
done
exit 0

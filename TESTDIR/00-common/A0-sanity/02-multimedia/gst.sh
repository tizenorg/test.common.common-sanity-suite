#!/bin/bash -x

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Authors : Ewan le Bideau Canevet <ewan.lebideau-canevet@open.eurogiciel.org>
#           Nicolas Zingile <nicolas.zingile@open.eurogiciel.org>


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

wait $pid

if [[ (( $? == 137 )) || (( $? == 143 )) || (( $? == 0 )) ]]; then
    exit 0
else
    echo "a core dump has occured, test failed" && exit 1
fi

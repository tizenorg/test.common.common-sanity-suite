#!/bin/bash
#
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
# Authors: Nicolas Zingile <nicolas.zingile@open.eurogiciel.org>


#--- some util functions to retrieve test user ---#

function gettestuser()
{
    local testuser=""

    if [[ -n $(getent passwd guest) ]]; then
	testuser=guest
    elif [[ -n $(getent passwd app) ]]; then
	testuser=app
    else
	echo "No suitable user" && exit 1
    fi

    echo $testuser 
}

function gettestprocess ()
{
    local testprocess=""
    
    if [[ -z $1 ]]; then
	echo "A user should be defined" && exit 1
    else
	case $1 in
	    "guest")
		testprocess=tz-launcher
		;;
	    "app")
		testprocess=weston-desktop
		;;
	    *)
		echo "Cannot get the process" && exit 1
	esac
	echo $testprocess
    fi
}

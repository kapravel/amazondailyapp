#!/bin/bash
function gnome-keyring-control() {
	local -a vars=( \
		DBUS_SESSION_BUS_ADDRESS \
		GNOME_KEYRING_CONTROL \
		GNOME_KEYRING_PID \
		XDG_SESSION_COOKIE \
	)
	local pid=$(ps -C gnome-session -o pid --no-heading)
	eval "unset ${vars[@]}; $(printf "export %s;" $(sed 's/\x00/\n/g' /proc/${pid//[^0-9]/}/environ | grep $(printf -- "-e ^%s= " "${vars[@]}")) )"
}

gnome-keyring-control
python `dirname $0`/amazon.py

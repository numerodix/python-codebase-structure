#!/bin/bash

dir="$1";shift;

if [ -z "$dir" ]; then
	echo "usage: $0 <dir>"
	exit 1
fi

find -type f -iname '*.py' -exec python {} \;

echo "Test successful if no exceptions were raised above ^"

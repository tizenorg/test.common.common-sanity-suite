#!/bin/bash -x
CMD="$@"
tmpscript=$(mktemp)
trap "rm -rf $tmpscript" INT QUIT TERM STOP EXIT
echo "#!/bin/bash " > $tmpscript
tr '\0' '\n' </proc/$(pgrep tz-launcher -u guest)/environ | awk 'FS="=" {if ($1 != "_") { print "export",$0;} }' >> $tmpscript
echo export PATH=$QAPATH:\$PATH >> $tmpscript
#echo env >> $tmpscript
echo $CMD >> $tmpscript
chmod 777 $tmpscript
su - guest -c $tmpscript
if [ $? -eq 0 ]; then
	exit 0
else
	exit 1
fi

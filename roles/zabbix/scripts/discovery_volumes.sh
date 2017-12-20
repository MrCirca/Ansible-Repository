#!/bin/bash
VOLUMES_LIST=`gluster --xml volume list`

GLUSTER_VOLUMES=$(echo -e "$VOLUMES_LIST" | grep -E "<volume>" | cut -d ">" -f 2 | cut -d "<" -f 1)

for GLUSTER_VOLUME_NAME in $GLUSTER_VOLUMES
do
	VOLUME_NAMES_JSON="$VOLUME_NAMES_JSON\n\t\t{\"{#GLUSTER_VOLUME_NAME}\": \"$GLUSTER_VOLUME_NAME\"},"
done

echo -e "{\n\t\"data\": [\n$VOLUME_NAMES_JSON\n\t]\n}"


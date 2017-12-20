#!/bin/bash
VOLUMES_LIST=`gluster --xml volume list`
HOSTNAME=`hostname -f`
GLUSTER_VOLUMES=$(echo -e "$VOLUMES_LIST" | grep -E "<volume>" | cut -d ">" -f 2 | cut -d "<" -f 1)

for GLUSTER_VOLUME_NAME in $GLUSTER_VOLUMES
do
        VOLUME_NAMES_JSON="$VOLUME_NAMES_JSON\n\t\t{\"{#GLUSTER_VOLUME_NAME}\": \"$GLUSTER_VOLUME_NAME\"},"
        BRICK_PATHS_JSON=`gluster --xml volume status $GLUSTER_VOLUME_NAME detail | grep -A 3 "$HOSTNAME" | grep "<path>" | cut -d ">" -f 2 | cut -d "<" -f 1`
        for BRICK_PATH_JSON in $BRICK_PATHS_JSON
        do
                BRICKS_JSON="$BRICKS_JSON\n\t\t{\"{#BRICK_PATH}\": \"$BRICK_PATH_JSON\", \"{#BRICK_VOLUME}\": \"$GLUSTER_VOLUME_NAME\"},"
        done
done

BRICKS_JSON=`echo $BRICKS_JSON | head -c -2`

echo -e "{\n\t\"data\": [\n$VOLUME_NAMES_JSON\n\t$BRICKS_JSON\n\t]\n}"


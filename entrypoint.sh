#!/bin/bash -l

python main.py --source ${SOURCE} --destination ${DESTINATION} --exclude ${EXCLUDE} --include ${INCLUDE} --delete ${DELETE} --dryrun ${DRYRUN}

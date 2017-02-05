#!/usr/bin/env bash

if [ $# -ne 3 ];then
    echo ""
    echo "please pass the parameters"
    echo "ex) create_diff_sample.sh OK_dir NG_dir diff_dir"
    echo ""
    exit 1
fi


#Parameters
ok_datapath=$1/
ng_datapath=$2/
diff_datapath=$3/

#SetupDirs
#mkdir outputdir
rm -rf $diff_datapath
mkdir -p $diff_datapath

#Create true image
for filename in $ok_datapath/*;do
    #Create Damged Image
    diff_filename=$(basename $filename)
    
    ./diff_image.py $filename $ng_datapath/$(basename $filename) $diff_datapath/$(basename $filename)
done

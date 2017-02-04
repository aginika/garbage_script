#!/usr/bin/env bash

if [ $# -lt 2 ];then
    echo ""
    echo "please pass the parameters"
    echo "ex) create_pix2pix_sample.sh input_datapath output_datapath (test_datapath val_datapath)"
    echo ""
    exit 1
fi

#Parameters
input_datapath=$1/
output_datapath=$2/
train_output_dir=$output_datapath/train
test_output_dir=$output_datapath/test
val_output_dir=$output_datapath/val

damaged_dir=$output_datapath/damaged

#SetupDirs
#mkdir outputdir
rm -rf $train_output_dir $test_output_dir $val_output_dir $damaged_dir
mkdir -p $2
mkdir -p $test_output_dir
mkdir -p $val_output_dir
mkdir -p $train_output_dir
mkdir -p $damaged_dir

#Create true image
for filename in $input_datapath/*;do
    #Create Damged Image
    damaged_filename=$damaged_dir/$(basename $filename)_damaged.png
    output_filename=$(basename $filename)
    
    ./damage_image.py $filename $damaged_filename 1

    #Convert to concatenated Image
    convert +append $damaged_filename $filename $train_output_dir/$output_filename
done

if [ $# -gt 2 ]; then
    for filename in $test_datapath/*;do
    #Create Damged Image
	damaged_filename=$damaged_dir/$(basename $filename)_damaged.png
	output_filename=$(basename $filename)
	
	./damage_image.py $filename $damaged_filename 1
	
    #Convert to concatenated Image
	convert +append $damaged_filename $filename $test_output_dir/$output_filename
    done
fi

if [ $# -gt 3 ]; then
    for filename in $val_datapath/*;do
    #Create Damged Image
	damaged_filename=$damaged_dir/$(basename $filename)_damaged.png
	output_filename=$(basename $filename)
	
	./damage_image.py $filename $damaged_filename 1
	
    #Convert to concatenated Image
	convert +append $damaged_filename $filename $val_output_dir/$output_filename
done
fi

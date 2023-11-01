rave preprocess --input_path /scratch/users/annammc/maestro/maestro-v3.0.0/2004 --output_path /scratch/users/annammc/output
export CUDA_VISIBLE_DEVICES=4
rave train --config v2 --db_path /scratch/users/annammc/output/ --name maestro

# rave export --run /path/to/your/run (--streaming)

# cp -r myrave $HOME/
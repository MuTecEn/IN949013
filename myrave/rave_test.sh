rave preprocess --input_path /scratch/users/annammc/maestro/maestro-v3.0.0/2004 --output_path /scratch/users/annammc/output

rave train --config v2 --db_path /scratch/users/annammc/output/data.mdb --name maestro

# rave export --run /path/to/your/run (--streaming)

# cp -r myrave $HOME/
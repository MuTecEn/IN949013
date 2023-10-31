# module load Anaconda3/5.3.0
module load FFmpeg/4.3.2-GCCcore-10.3.0

module load Python/3.9.6-GCCcore-11.2.0
# python -m venv ./raveenv
source ./raveenv/bin/activate

nohup python -u ravev2_training.py run --username annammc > /logs/ravev2_training.log 2>&1 & echo $! > annammc.pid

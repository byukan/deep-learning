#9/25{
added some slides on multi-label classification to this page https://learn.galvanize.com/cohorts/182/units/2420/content_files/45970

https://stats.stackexchange.com/questions/95495/guideline-to-select-the-hyperparameters-in-deep-learning

we will be using GCP this week. Please follow these two tutorials to get set up

1. http://cs231n.github.io/gce-tutorial/
2. http://cs231n.github.io/gce-tutorial-gpus/

Stanford course on Tensorflow: http://web.stanford.edu/class/cs20si/syllabus.html

	conda create -n py36 python=3.6

    if u got the insecurerequest warning doing the conda create
sudo pip install -U requests
and then conda create step

Scalar Dense
https://vimeo.com/219794678

https://betterexplained.com/articles/intuitive-trigonometry/

https://www.youtube.com/watch?v=GZTvxoSHZIo&feature=youtu.be&t=48m13s



# steps to install

# https://cloud.google.com/sdk/docs/quickstart-mac-os-x

#yours might have a different project and server name
gcloud compute --project “dsci6005” ssh --zone “us-west1-b” “instance-1”


# execute this on google cloud machine
alias python=python3

which python # should be python3.7

wget https://repo.continuum.io/archive/Anaconda3-4.4.0-MacOSX-x86_64.sh
bash Anaconda3-4.4.0-MacOSX-x86_64.sh 

sudo pip install keras

wget https://s3-us-west-2.amazonaws.com/learn.galvanize.com/learn-files/gSchool/DSCI6005/master/docker/environment.yml
conda env create --force
source activate dl

wget https://raw.githubusercontent.com/fchollet/keras/master/examples/mnist_mlp.py
python mnist_mlp.py
}
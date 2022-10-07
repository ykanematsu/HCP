FROM ubuntu:latest

# install linux commands
RUN apt-get -y update && apt-get install -y \
sudo wget vim curl bzip2 unzip libxext-dev libxrender1

# add Japanese packages to ubuntu
RUN apt-get install -y language-pack-ja-base language-pack-ja \
fontconfig fonts-takao && locale-gen ja_JP.UTF-8

# install miniconda3-py3.9
COPY ./ /work
WORKDIR /work
ARG version="latest"
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-${version}-Linux-x86_64.sh && \
sh /work/Miniconda3-${version}-Linux-x86_64.sh -b -p /opt/miniconda3 && \
rm -f Miniconda3-${version}-Linux-x86_64.sh

# set path
ENV PATH /opt/miniconda3/bin:$PATH

# install libraries
RUN conda install conda && \
#conda install --file conda_requirements.txt
conda install -c conda-forge rdkit lightgbm shap gunicorn && \
conda install -c bioconda pubchempy && \
conda install numpy pandas flask scikit-learn
##conda install -c rdkit -c mordred-descriptor mordred && \
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]

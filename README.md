create env

'''bash
conda create -n wineq python==3.7 -y
'''

activate env

'''bash
conda activate wineq
'''

created req

install requirements

'''bash
pip install -r requirements.txt
'''

download the data from:
http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

git init

dvc init

dvc add data_given/winequality-red.csv

git add .

git commit -m "first commit"

oneliner update for readme
git add . && git commit -m "update readme.md"


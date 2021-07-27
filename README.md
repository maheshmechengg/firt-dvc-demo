create env

```bash
conda create -n wineq python==3.7 -y
```

activate env

```bash
conda activate wineq
```

created req

install requirements

```bash
pip install -r requirements.txt
```

download the data from:
http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality-red.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
oneliner update for readme
```bash
git add . && git commit -m "update readme.md"
```
after creating git repository below
```bash
git remote add origin https://github.com/maheshmechengg/firt-dvc-demo
git branch -M main
git push origin main
```

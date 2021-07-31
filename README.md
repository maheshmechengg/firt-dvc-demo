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


```bash
git clone -b main-mlflow https://github.com/maheshmechengg/firt-dvc-demo.git

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
get dvc metrics
```bash
dvc metrics show
```
get dvc difference
```bash
dvc metrics diff
```
install test requirements
```bash
pip install pytest
```
install tox
```bash
pip install tox
```

tox command
```bash
tox
```

for rebuilding
```bash
tox -r
```

pytest command
```bash
pytest -v
```
setup command, after making setup file
```bash
pip install -e .
```
build your own package as Pypy
```bash
python setup.py sdist bdist_wheel
```

create an artifacts folder
```bash
mkdir artifacts
````

mlflow server command
```bash
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0
```


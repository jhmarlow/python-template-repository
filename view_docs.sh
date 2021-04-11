echo Building docs...

cd docs

sphinx-build -b html source build

python3 -m http.server
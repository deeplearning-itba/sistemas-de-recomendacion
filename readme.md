# Instalación de dependencias
```bash
conda create -n sistemas-de-recomendacion python=3.9
conda activate sistemas-de-recomendacion

pip install -r requirements.txt
```

# Bajada y descompresión de la data
Si el archivo no esta en el repo bajarlo de: http://files.grouplens.org/datasets/movielens/ml-100k.zip
 ```bash
 wget http://files.grouplens.org/datasets/movielens/ml-100k.zip
 unzip ml-100k.zip
 ```
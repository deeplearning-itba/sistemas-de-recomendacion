``` bash
docker pull opensearchproject/opensearch

cd vecctor_db
docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" -d -v /Users/julian/Documents/repos/sistemas-de-recomendacion/vector_db/db_data:/usr/share/opensearch/data opensearchproject/opensearch:latest

docker ps

docker exec -it opensearch-node /bin/bash

docker kill 
```

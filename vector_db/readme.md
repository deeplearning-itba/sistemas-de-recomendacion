``` bash
docker pull opensearchproject/opensearch

cd vector_db
docker run -it -p 9200:9200 -p 9600:9600 -e "plugins.security.disabled=true" -e OPENSEARCH_INITIAL_ADMIN_PASSWORD=PassWord#1234! -e "discovery.type=single-node" --name opensearch-node opensearchproject/opensearch:latest


docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" -d -v /Users/julian/Documents/repos/sistemas-de-recomendacion/vector_db/db_data:/usr/share/opensearch/data opensearchproject/opensearch:latest


docker run -it -p 9200:9200 -p 9600:9600 -e "plugins.security.disabled=true" -e OPENSEARCH_INITIAL_ADMIN_PASSWORD=PassWord#1234! -e "discovery.type=single-node" -v /Users/julian/Documents/repos/sistemas-de-recomendacion/vector_db/db_data:/usr/share/opensearch/data opensearchproject/opensearch:latest

docker ps

docker exec -it opensearch-node /bin/bash

docker kill 
```

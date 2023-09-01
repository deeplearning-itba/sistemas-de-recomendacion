# %%
from opensearchpy import Field, Float, Integer, Document, Keyword, Text, DenseVector, Nested, Date, Object
from opensearchpy import OpenSearch
import numpy as np
import pandas as pd
import datetime
# %%
header = ['userId', 'movieId', 'rating', 'timestamp']
df_movies = pd.read_csv('../ml-100k/u.item', sep='|', names=['id', 'name', '#', 'url'] + list(range(20)) , encoding='latin-1')
df_users = pd.read_csv('../ml-100k/u.user', sep='|',  names=['id', 'age', 'ocupation', ''], encoding='latin-1')
# %%

# %%
movie_embeddings_matrix = np.load('../vectors/movie_embeddings_matrix.npy')
user_embeddings_matrix = np.load('../vectors/user_embeddings_matrix.npy')
user2Idx = np.load('../vectors/user2Idx.npy', allow_pickle=True).item()
movie2Idx = np.load('../vectors/movie2Idx.npy', allow_pickle=True).item()

# %%
df_users['userIdx'] = df_users['id'].apply(lambda x: user2Idx[x])
df_movies['movieIdx'] = df_movies['id'].apply(lambda x: movie2Idx[x])
# %%
df_movies
# %%
movie_embeddings_matrix.shape[1]
# %%
host = 'localhost'
port = 9200
auth = ('admin', 'admin')

client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
)
# %%
client.cluster.health()
# %%
client.indices.delete('movie')
# %%


class KNNVector(Field):
    name = "knn_vector"
    def __init__(self, dimension, method, **kwargs):
        super(KNNVector, self).__init__(dimension=dimension, method=method, **kwargs)

method = {
    "name": "hnsw",
    "space_type": "cosinesimil",
    "engine": "nmslib"
}
# %%
index_name = 'movie'
class Movie(Document):
    movie_id = Keyword()
    created_at = Date()
    vector = KNNVector(
        movie_embeddings_matrix.shape[1],
        method
    )
    class Index:
        name = index_name
        settings = {
                'index': {
                'knn': True
            }
        }

    # def save(self, ** kwargs):
    #     self.meta.id = self.movie_id
    #     return super(Movie, self).save(** kwargs)
# %%
Movie.init(using=client)
# %%
# %%
for i, row in df_movies.iterrows():
    mv = Movie(
        movie_id = row.id,
        vector = list(movie_embeddings_matrix[row.movieIdx]),
        creared_at = datetime.datetime.now()
    )
    mv.save(using=client)
    
    
# %%
Movie.search(using=client).count()
# %%
query = {
        "size": 20,
        "query": {
            "knn": {
            "vector": {
                "vector": movie_embeddings_matrix[5],
                "k" : 5
            }
            }
        }
        }
# %%
response = client.search(index='movie', body=query)
# %%
response

# %%

import gensim

path = './model/idwiki_word2vec.model'
id_w2v = gensim.models.word2vec.Word2Vec.load(path)
# print(id_w2v.most_similar('raja'))
print(id_w2v)

# import gensim
# print(gensim.__version__)
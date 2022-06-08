import pickle




def check_review(textData):
    file = open("pickle_model.pkl", 'rb')

    recreated_model = pickle.load(file)
    
    #load the vocab
    
    vocab = pickle.load((open('features.pkl', 'rb')))
    
    from sklearn.feature_extraction.text import CountVectorizer
    recreated_vec = CountVectorizer(decode_error ='replace' ,vocabulary = vocab)

    from sklearn.feature_extraction.text  import TfidfTransformer
    
    transformer = TfidfTransformer()
    
    return recreated_model.predict(transformer.fit_transform(recreated_vec.fit_transform([textData])))
    

    
  
check_review("I loved that product and very useful")
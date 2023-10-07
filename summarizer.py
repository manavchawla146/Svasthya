
try:



    def read_article(file):
        f=open(file,"r")
        filedata=f.readlines()
        ar=filedata[0].split(".")
        sen=[]
        for sen in ar:
            sen.append(sen.replace("[^a-zA-Z"," ").split(" "))
        sen.pop()
        return sen

    def sentence_similar(sen1,sen2,stopwords=None):
        if stopwords is None:
            stopwords=[]
        sen1= [w.lower() for w in sen1]
        sen2= [w.lower() for w in sen2]
        all_words=list(set(sen1+sen2))

        vec1=[0] * len(all_words)
        vec2=[0] * len(all_words)
        for w in sen1:
            if w in stopwords:
                continue
            vec1[all_words.index(w)] +=1
        for w in sen2:
            if w in stopwords:
                continue
            vec2[all_words.index(w)] +=1

        return 1-cosine_distance(vec1,vec2)

    def gen_sim_mat(sentence,op):
        similarity_mat=np.zeroes((len(sentences),len(sentences)))
        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1==idx2:
                    continue
                simillarity_mat[idx1][idx2]=sentence_similar(sentences[idx1],sentences[idx2],op)
        return simillarity_mat

    def generate_summary(file_name,top_n=5):
        op=stopwords.words('english')
        summarize_text=[]
        sentences=read_article(file_name)
        sentence_similarity_matrix=gen_sim_mat(sentences,op)
        sentence_similarity_graph=nx.from_numpy_array(sentence_similarity_matrixs)
        scores=nx.pagerank(sentence_similarity_graph)
        ranked_sentences=sorted(((scores[i],s)for i,s in enumerate(sentences)),reverse=True)
        for i in range(top_n):
            summarize_text.append(" ".join(ranked_sentences[i][1]))
        print("Summary \n",". ".join(summarize_text))


    generate_summary("testcase.txt")


































except:
    print("")




import random
lst1=[["artificial intellegence", "robots","human like machine","truth","principles","algorithm","simple","complex","mimic","human cognitive activity","learning","reasoning","perception","develop systems","skeptical","cognitive","value judgements","human experience"],["perception","human experience","reasoning","complex","robots","skeptical"],["value judgements","human experience","reasoning","artificial intellegence"]]
print(random.choice(lst1))

      

import math

class MultinomialNB:
    def __init__(self, articles_per_tag):
        # Don't change the following two lines of code.
        self.articles_per_tag = articles_per_tag  # See question prompt for details.
        self.train()

    def train(self):
        tagP = [[0] for x in range(3)]
        sum = 0
        st = set()
        for p, q in self.articles_per_tag.items():
            for pq in range(len(q)):
                for qp in range(len(q[pq])):
                    st.add(q[pq][qp])
        for tag, article in self.articles_per_tag.items():
            sum += len(article)
            if tag == "politics":
                tagP[0] = len(article)
            elif tag == "sports":
                tagP[1] = len(article)
            elif tag == "tech":
                tagP[2] = len(article)
        tagP[0], tagP[1], tagP[2] = math.log(tagP[0]/sum), math.log(tagP[1]/sum), math.log(tagP[2]/sum)
        test = {}
        self.tags = tagP
        for ss in st:
            test[ss] = []
        probs = {"politics": [], "sports": [], "tech": []}
        for it in st:
            for t, a in self.articles_per_tag.items():
                nom = 0
                denom = 0
                for j in range(len(a)):
                    denom += len(a[j])
                    for k in range(len(a[j])):
                        if a[j][k] == it:
                            nom += 1
                if t == "politics":
                    test[it].append([t, tagP[0], nom + 1, (denom) + 2, (nom + 1)/ ((denom) + 2)])
                elif t == "sports":
                    test[it].append([t, tagP[1], nom + 1, (denom) + 2, (nom + 1)/ ((denom) + 2)])
                elif t == "tech":
                    test[it].append([t, tagP[2], nom + 1, (denom) + 2, (nom + 1)/ ((denom) + 2)])
                nom = 0
                denom = 0
        self.articles_per_tag = test

    def predict(self, article):
        probs = {"politics": [], "sports": [], "tech": []}
        for it in article:
            if self.articles_per_tag.get(it) != None:
                for k in range(len(self.articles_per_tag[it])):
                    probs[self.articles_per_tag[it][k][0]].append(math.log(self.articles_per_tag[it][k][4]))
            elif self.articles_per_tag.get(it) == None:
                probs["politics"].append(math.log(0.5))
                probs["sports"].append(math.log(0.5))
                probs["tech"].append(math.log(0.5))
        sum_p, sum_s, sum_t = 0, 0, 0
        for a, b in probs.items():
            if a == "politics":
                sum_p = sum(b)
            elif a == "sports":
                sum_s = sum(b)
            elif a == "tech":
                sum_t = sum(b)
        ans = {"politics": self.tags[0] + sum_p, "sports": self.tags[1] + sum_s, "tech": self.tags[2] + sum_t}
        return ans

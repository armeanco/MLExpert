def probability_of_disease(accuracy, prevalence):
    pos = prevalence*accuracy / ((prevalence*accuracy) + (1-prevalence) * (1-accuracy))
    neg = (1-prevalence) * accuracy / ((prevalence* (1-accuracy)) + ((1-prevalence) * accuracy))
    return [pos * 100, neg * 100]

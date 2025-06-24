def average(scores):
    total_scores=0
    for s in scores:
        total_scores+=scores[s]
    return total_scores/len(scores)


class_3B={
    "marine" : 18,
    "jean" : 15,
    "coline" :8,
    "luc" : 9
}

class_3C={
    "quentin" : 17,
    "julie" : 15,
    "marc" : 8,
    "stephanie" : 13
}

print(f"Average for Class 3B : {average(class_3B)} .")
print(f"Average for Class 3C : {average(class_3C)} .")
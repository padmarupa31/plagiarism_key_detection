def classify_similarity(score):
    percentage = score * 100

    if percentage < 30:
        return "Low Plagiarism"
    elif percentage < 60:
        return "Moderate Plagiarism"
    else:
        return "High Plagiarism"

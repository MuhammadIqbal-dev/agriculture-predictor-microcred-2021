

coef = -51.36637103
intercept = 111115.3745066
def predict(year):
    predicted_value = coef*year + intercept
    print(predicted_value)
    return predicted_value
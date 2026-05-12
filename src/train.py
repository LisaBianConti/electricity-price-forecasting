def train_regression(model, X_train, y_train):

    model.fit(X_train, y_train)
    
    return model
def maker(N):
    def action(X):
        return X**N

    return action

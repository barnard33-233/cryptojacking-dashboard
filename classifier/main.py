from classify import classifier, init

if __name__ == '__main__':
    df_test = init()
    classifier(df_test)

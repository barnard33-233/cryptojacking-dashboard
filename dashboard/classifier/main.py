from classify import classifier, init

if __name__ == '__main__':
    df_test = init()
    print(df_test)
    classifier(df_test)

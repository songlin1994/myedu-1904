import yaml

if __name__ == '__main__':
    # f = open('test.yaml', encoding="utf-8")
    # d = yaml.load(f,Loader=yaml.FullLoader)
    # print(d)

    a = {1:2}
    b = a
    a[3]=  4
    print(b)
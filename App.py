import json

def main(args=[]):

    f = open("contatos.txt", encoding = "utf8")
    jsonObject = json.loads(f.read())
    print(jsonObject)

if __name__ == '__main__':
    main()

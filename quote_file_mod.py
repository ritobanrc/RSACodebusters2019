import csv
from random import choice

def get_quotes(file_name="randomquotes.csv"):
    with open(file_name, "r") as f:
        dat = csv.reader(f, delimiter=';')
        e=[r[0]+' - '+ r[1] for r in dat]
        return e
def get_quote():
    return choice(get_quotes())
if __name__ == "__main__":
    t = get_quotes()
    for i in range(10):
        print(str(i)+'. ' + choice(t))

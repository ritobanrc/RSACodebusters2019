from random import choice
import csv

books='Genesis,Exodus,Leviticus,Numbers,Deuteronomy,Joshua,Judges,Ruth,Samuel 1,Samuel 2,Kings 1,Kings 2,Chronicles 1,Chronicles 2,Ezra,Nehemiah,Esther,Job,Psalms,Proverbs,Ecclesiastes,Song of Solomon,Isaiah,Jeremiah,Lamentations,Ezekiel,Daniel,Hosea,Joel,Amos,Obadiah,Jonah,Micah,Nahum,Habakkuk,Zephaniah,Haggai,Zechariah,Malachi,Matthew,Mark,Luke,John,Acts,Romans,Corinthians 1,Corinthians 2,Galatians,Ephesians,Philippians,Colossians,Thessalonians 1,Thessalonians 2,Timothy 1,Timothy 2,Titus,Philemon,Hebrews,James,Peter 1,Peter 2,John 1,John 2,John 3,Jude,Revelation'.split(',')

def get_quotes(bible="bible.csv"):
    with open(bible, 'r') as f:
        dat = csv.reader(f, delimiter=',')
        e = []
        for r in dat:
            e.append(r[4] + ' - '+ books[int(r[1])-1] + ' Chapter '+ str(r[2])+ ' Verse '+ str(r[3]))
        return e

if __name__ == "__main__":
    r = get_bible()
    for i in range(10):
        print(str(i+1)+'. '+choice(r))

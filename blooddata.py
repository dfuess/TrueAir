from glob import glob
from os.path import getctime
from datetime import datetime
from sqlite3 import connect as sqlconnect
import matplotlib.pyplot as plt
from calendar import monthrange

DEBUG = False
DataSet = None #r"C:\Users\david\Dropbox\Python\TrueAir\data\TrueManagerAir APR-27-2023 040009 AM.tmx"
de_datetime = 0
de_glucose_value = 1
mask = r'C:\Users\david\Dropbox\Python\TrueAir\data\*.tmx'
fetch_sql = "SELECT de_datetime/1000, de_glucose_value FROM dataEntryItems"
AM = [0, 12]
PM = [12, 24]


def between(x, vals):
    return x >= min(vals) and x <= max(vals)




class BloodData:
    def __init__(self, database = None):
        # alldata = {'dt':[], 'month':[], 'hour':[], 'time':[], 'data':[]}
        self.database = database
        self.rawdata = []
        self.data = []
        self.subset = []
        self.currentyear = datetime.now().year
        self.open(database)

    def open(self, database=None):
        if database:
            self.database = database
        if self.database is None:
            files = glob(mask)
            latest = 0
            for f in files:
                t = getctime(f)
                if t > latest:
                    latest = t
                    self.database = f
            if self.database is None:
                print("No database found")
                exit(1)

        if DEBUG: print(f"Database: {self.database}")
        conn = sqlconnect(self.database)
        c = conn.cursor()
        c.execute(fetch_sql)
        if DEBUG: print(f"Opened database: {self.database}")
        self.rawdata = c.fetchall()

        for entry in self.rawdata:
            dt = datetime.fromtimestamp(int(entry[de_datetime]))
            self.data.append([dt, entry[de_glucose_value]])
        return len(self.data)

    def getDataRange(self, start=None, stop=None, years=None, months=None, days=None, hours=None):
        if start is None or stop is None:
            if years is None:
                years = [self.currentyear, self.currentyear]
            if months is None:
                months = [1, 12]
            if days is None:
                days = [1, 31]
            if hours is None:
                hours = [0, 24]

            start = datetime(years[0], months[0], days[0])
            stop = datetime(years[1], months[1], monthrange(years[1], months[1])[1])

        self.subset = [self.data[i] for i in range(len(self.data)) if not (self.data[i][0] < start or self.data[i][0] > stop)]
        dataset = [self.subset[i] for i in range(len(self.subset)) if between(self.subset[i][0].hour, hours)]
        return dataset

    def XY(self, data):
        X = []
        Y = []
        for d in data:
            X.append(d[0])
            Y.append(d[1])
        return X, Y


if __name__ == '__main__':
    db = BloodData()
    y = datetime.now().year
    m = datetime.now().month
    # any = db.getDataRange()
    # pprint.pprint(any)
    am = db.getDataRange(years=[y, y], months=[1, m], hours=[0, 12])
    pm = db.getDataRange(years=[y, y], months=[1, m], hours=[12, 24])

    # pprint.pprint(am)
    # pprint.pprint(pm)

    fig, (ax0) = plt.subplots(1)

    ax0.set_ylabel("Sugar (mg/dl)")
    ax0.set_xlabel("Date")
    ax0.set_title("Blood Sugar")

    xa, ya = db.XY(am)
    if DEBUG: print(ya)
    ax0.plot(xa, ya, 'ro-', label="AM", linewidth=1, markersize=5)

    xp, yp = db.XY(pm)
    if DEBUG: print(yp)
    ax0.plot(xp, yp, 'bx-', label="PM", linewidth=1, markersize=5)
    ax0.legend()

    plt.show()
    # for d,g in xd:
    #     print(f"{d.strftime('%b %d %Y %H:%M:%S')} {g:3d}")
    #pprint.pprint(RD)
    # months = set(AD['month'])
    # print("Data Summary")
    # print("Mo  AM   (  +/- , n)    PM   (  +/- , n)    All  (  +/- , n)")
    # for m in months:
    #     am = AD['data'][AD['month']==m][AD['time']=='AM']
    #     pm = AD['data'][AD['month']==m][AD['time']=='PM']
    #     al = AD['data'][AD['month']==m]
    #
    #     print(f"{m:2} {np.mean(am):6.2f}({np.std(am):6.2f},{len(am):2})"
    #           f" | {np.mean(pm):6.2f}({np.std(pm):6.2f},{len(pm):2})"
    #           f" | {np.mean(al):6.2f}({np.std(al):6.2f},{len(al):2})")

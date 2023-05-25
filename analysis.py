from blooddata import BloodData
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from datetime import datetime, timedelta
import numpy as np

DEBUG = False
a1c = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]
eag = [97, 111, 126, 140, 154, 169, 183, 197, 212, 226, 240, 255, 269, 283, 298]


def poly1(x, a, b, ):
    return a * x + b


def poly2(x, a, b, c):
    return a * x * x + b * x + c


def poly3(x, a, b, c, d):
    return a * x * x * x + b * x * x + c * x + d


def plotFit(parm, xdata, ydata, func, label, note):
    def dt(timediff):
        return timediff.days+timediff.seconds/86400.
    if len(ydata) == 0:
        return
    xfit = [dt(xdata[i]-xdata[0]) for i in range(len(xdata))]
    # print(xfit)
    popt, pcov = curve_fit(func, xfit, ydata)
    plt.plot(xdata, ydata, parm[1], linewidth=1, markersize=5, label=note)
    plt.plot(xdata, func(np.array(xfit), *popt), parm[0], linewidth=1, label=label)  # % tuple(popt))
    plt.xlabel('Date')
    plt.ylabel('Sugar (mg/dl)')
    plt.legend()


def fitData(fit_type, xdata, ydata, parm, note):
    if fit_type == 'Linear':
        plotFit(parm, xdata, ydata, poly1, f'{fit_type} fit', note)  #: Cov=%5.3f, b=%5.3f', note)
    elif fit_type == 'Quadratic':
        plotFit(parm, xdata, ydata, poly2, f'{fit_type} fit', note)  #: Cov=%5.3f, b=%5.3f, c=%5.3f', note)
    elif fit_type == 'Cubic':
        plotFit(parm, xdata, ydata, poly3, f'{fit_type} fit', note)  #: Cov=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f', note)


def plotBloodData(db, fit_type, n, am=None, pm=None, years=None, months=None, noplot=False):
    # Arguments
    # db     =  instance of BloodData
    # fit_type = the fit function: Linear, Quadratic, or Cubic
    # n      =  The plot frame to use
    # am     = blood data for AM
    # pm     = blood data for PM
    # years  = the range of years [from, to] or a single year [year]
    # months = the range of months [from, to] or a single month [month]
    # You must provide either am & pm or years & months but do not mix them.
    f = interp1d(eag, a1c)
    haveym = years is not None and months is not None
    if am is None and haveym:
        am = db.getDataRange(years=years, months=months, hours=[0, 12])
    if pm is None and haveym:
        pm = db.getDataRange(years=years, months=months, hours=[12, 24])
    delta = (am[-1][0] - am[0][0]).days + 1
    xa, ya = db.XY(am)
    xp, yp = db.XY(pm)
    avg_am = np.mean(ya)
    avg_pm = np.mean(yp)
    avg = np.mean([avg_am, avg_pm])
    plt.figure(n)

    fitData(fit_type, xa, ya, ["r-", "mP-"], f"Actual AM")
    fitData(fit_type, xp, yp, ["b-", "kx-"], f"Actual PM")
    title = f"Blood Data (Avg: AM: {avg_am:.0f}, PM: {avg_pm:.0f}, Mean: {avg:.0f}, A1C:{f(avg_am):.2f}) ({delta} days)"
    plt.title(title)
    if not noplot:
        plt.show()
    return title


if __name__ == '__main__':
    db = BloodData()
    date_end = datetime.now()

    frame = 1
    for days in [7, 30, 90, 365]:
        date_start = date_end - timedelta(days=days)
        am_data = db.getDataRange(start=date_start, stop=date_end, hours=[0, 12])
        pm_data = db.getDataRange(start=date_start, stop=date_end, hours=[12, 24])
        plotBloodData(db, 'Cubic', frame, am_data, pm_data, noplot=True)
        frame += 1

    plt.show()

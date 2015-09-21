import cPickle
import pickle
import os
from contextlib import closing

class ATDB:

    def  __init__(self, domain):
        self.domain = domain

        self.dayidx = {}
        self.minidx = {}
        self.reportidx = {}
        self.infoidx = {}
        self.basepath = "E://listen//" + domain + "//"
        self.daypath = "day//"
        self.minpath = "min//"
        self.reportpath = "report//"
        self.config = {}

    def config_data(self):
        return self.config

    def save_config(self):
        filename = "%satsvr.cfg" % (self.basepath)
        with closing(open(filename,'wb')) as file:
            cPickle.dump(self.config, file)

    def min_data(self, id):
        """5 miniutes data"""
        pass

    def day_data(self, id):
        """day data"""
        if not self.dayidx.has_key(id):
            filename = "%s%s%s.day" % (self.basepath, self.daypath, id)
            print filename
            if os.path.exists(filename):
                with closing(open(filename,'rb')) as file:
                    self.dayidx[id] = cPickle.load(file)
            else:
                self.dayidx[id] = {}
        return self.dayidx[id]

    def report_data(self, id):
        """"realtime data"""
        pass

    def info_data(self, id):
        """information today"""
        pass

    def save_day_data(self, id):
        filename = "%s%s%s.day" % (self.basepath, self.daypath, id)
        with closing(open(filename,'wb')) as file:
            cPickle.dump(self.dayidx[id], file)

    def save_min_data(self, id):
        filename = "%s%s%s.min" % (self.basepath, self.minpath, id)
        with closing(open(filename,'wb')) as file:
            cPickle.dump(self.minidx[id], file)

    def save_report_data(self, id):
        filename = "%s%s%s.rep" % (self.basepath, self.reportpath, id)
        with closing(open(filename,'wb')) as file:
            cPickle.dump(self.reportidx[id], file)

def test():
    db = ATDB("sh")
    a = db.day_data("000001")
    print a
    a[20150112] = {'x':12,'y':23,'z':69}
    db.save_day_data("000001")

if __name__ == '__main__':
    test()

from common import log

import clean
import export
import model
import organize

if __name__ == '__main__':

    log.init()
    model.create_tables()
    export.export("./source/stock.csv")
    clean.clean("./source/stock.csv")
    organize.organize()

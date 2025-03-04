class Salary:
    def __init__(t, basic, hra, pf):
        t.basic = basic
        t.hra = hra
        t.pf = pf
        t.total = basic + hra - pf
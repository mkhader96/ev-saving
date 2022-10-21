class Ev_Saving:
    def __init__(self):
        self.avg_ev = 0.2
        

    
    def electic_bill(support,spend):
        if support == 'y':
            if spend <= 300:
                return spend * 0.05
            elif spend <= 600:
                return (spend - 300) * 0.1 + 15
            elif spend > 600:
                return (spend - 600) * 0.2 + 45
            
            
        else:
            if spend <= 1000:
                return spend * 0.12
            elif spend > 1000:
                return (spend - 1000) * 0.15 + 120


    def increased_electricity(self,monthly_km):
        return monthly_km * self.avg_ev
    def before_bill(self, bill_support, electricity_spend):
        return Ev_Saving.electic_bill(bill_support, electricity_spend)
import datetime


class QuitTracker:
    def __init__(self, years_of_smoking,
                 quit_date,
                 quit_time,
                 smoked_cigarettes_per_day,
                 cigarettes_in_pack,
                 price_per_pack,
                 currency
                 ):
        """
        :param int years_of_smoking: How many years have you been smoking 
        :param str quit_date: Your quit date - ("yyyy/mm/dd")
        :param str quit_time: Your quit time - ("Hour:Minute")
        :param int smoked_cigarettes_per_day: Average number of cigarettes smoked per day
        :param int cigarettes_in_pack: Number of cigarettes in a pack
        :param int price_per_pack: Price of a pack of cigarettes
        :param str currency: Currency symbol

        """
        self.years_of_smoking = int(years_of_smoking)
        self.quit_date = quit_date # yyyy/mm/dd
        self.quit_time = quit_time # hh:ss
        self.smoked_cigarettes_per_day = int(smoked_cigarettes_per_day)
        self.cigarettes_in_pack = int(cigarettes_in_pack)
        self.price_per_pack = int(price_per_pack)
        self.currency = currency
        self.smoke_free_seconds = self.not_smoke_time()
        ###

    @staticmethod
    def seconds_to_time(time):
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        return [day, hour, minutes, seconds]

    def not_smoke_time(self):
        year, month, day = self.quit_date.split("/")
        hour, minute = self.quit_time.split(":")
        a = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        b = datetime.datetime.now()
        return round((b-a).total_seconds()) # seconds
    
    def smoke_free(self):
        time = self.smoke_free_seconds
        return self.seconds_to_time(time)
            
    def cigarettes_not_smoked(self):
        not_smoking = 86400/ self.smoked_cigarettes_per_day
        time = self.smoke_free_seconds
        return round(time/not_smoking, 2)
    
    def money_saved(self):

        time = self.smoke_free_seconds
        total_price = (time*int(self.price_per_pack))/84600
        return round(total_price, 2)
    
    
    def life_regained(self):
        ns = self.cigarettes_not_smoked()
        time = round(ns*11*60) # seconds
        return self.seconds_to_time(time)


    ## 

    def smoked_cigarettes(self):
        return self.years_of_smoking * 365 * self.smoked_cigarettes_per_day
    
    def money_wasted(self):
        return self.years_of_smoking * 365 * self.price_per_pack
    
    def life_lost(self):
        smoked_cigarettes = self.smoked_cigarettes()
        time = smoked_cigarettes*11*60

        return self.seconds_to_time(time)

    def percentage(self):
        ach = {
            86400:"1 Day",
            172800:"2 Days",
            259200:"3 Days",
            432000:"5 Days",
            604800:"7 Days",
            1209600:"14 Days",
            2592000:"1 Month",
            7776000:"3 Months",
            15552000:"6 Months",
            31536000:"1 Year",
            63072000:"2 Years",
            94608000:"3 Years",
            126144000:"4 Years",
            157680000:"5 Years",
            315360000:"10 Years",
            630720000:"20 Years",
            1576800000:"50 Years",
            2207520000:"70 Years",
            3153600000:"100 Years"
        }
        achievements_list = [86400, 172800, 259200, 432000,
                            604800, 1209600, 2592000, 7776000,
                            15552000, 31536000, 63072000, 94608000,
                            126144000, 157680000, 315360000, 630720000,
                            1576800000, 2207520000, 3153600000]
        # 1 day, 2 days, 3 days, 5 days, 7 days, 14 days, 1 month, 3 months, 6 months, 1 year, 2 years, 3 years, 5 years
        # 10 years, 20 years, 50 years, 70 years, 100 years
        time = self.smoke_free_seconds
        for tm in achievements_list:
            if time>tm:
                continue
            else:
                return [round(100/(157680000/time), 2), ach[tm]] # percentage and to time
                

    def life_expectancy(self, time):
        not_smoked_cigarettes = self.smoked_cigarettes_per_day * time
        tm = not_smoked_cigarettes*11*60
        day = tm // (24 * 3600)
        tm = tm % (24 * 3600)
        hour = tm // 3600
        tm %= 3600
        minutes = tm // 60
        return [day, hour, minutes]
    
    def money_expectancy(self, time):
        not_smoked_cigarettes = self.smoked_cigarettes_per_day * time
        money = (not_smoked_cigarettes/self.cigarettes_in_pack)*self.price_per_pack
        return money


        

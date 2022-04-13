from regex import E
import requests
import json
import datetime


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

class VaktijaEU():
    """
    VaktijaEU is a wrapper around the VaktijaEU API.
    """    
    
    def get_prayertimes(location_slug):
        """
        Returns the prayertimes for a given location.
        """
        url = f"https://api.vaktija.eu/v1/locations/slug/{location_slug}"
        result = {"success": False, "prayertimes": []}
        try:
            response = requests.get(url).json()
            months =  response["data"]["months"]
            timestamp = str(datetime.date.today().year)
            for month in months:
                current_month = str(month).zfill(2)
                for days in months[month]:
                    for day in months[month]["days"]:
                        current_day = str(day).zfill(2)
                        current_date =f"{timestamp}-{current_month}-{current_day}"
                        the_prayertimes = months[month]["days"][day]["prayers"]
                        result["prayertimes"].append({
                                 "date": current_date,
                                 "fajr": the_prayertimes[0],
                                 "sunrise": the_prayertimes[1],
                                 "dhuhr": the_prayertimes[2],
                                 "asr": the_prayertimes[3],
                                 "maghrib": the_prayertimes[4],
                                 "isha": the_prayertimes[5]
                             })
            result["success"] = True
            return result
            
        except Exception as e:
            print(e)
            return result
        
    def get_locations():
        """
        Returns the available locations.
        """
        try:
            file = open("app/static/vaktijaeu_locations.json", "r")
            return json.load(file)
        except:
            try:
                # Send a request to the VaktijaEU API to get the locations
                return requests.get("https://api.vaktija.eu/v1/locations").json()
            except:
                return None


class VaktijaBA():
    """
    VaktijaBA is a wrapper around the VaktijaBA API.
    """
    
    def get_prayertimes( id: int ):
        
        this_year = datetime.datetime.now().year
        result = {"success": False, "prayertimes": []}
        try:
            for year in range(this_year, (this_year + 2)):
                url = f"https://api.vaktija.ba/vaktija/v1/{id}/{year}"
                prayertimes_this_year = requests.get(url).json()["mjesec"]

                for index, month in enumerate(prayertimes_this_year):
                    for index2, day in enumerate(month["dan"]):

                        date = f"{year}-{str(index+1).zfill(2)}-{str(index2+1).zfill(2)}"
                        result["prayertimes"].append({
                                                    "date": date,
                                                    "fajr": str(day["vakat"][0]).zfill(2),
                                                    "sunrise": day["vakat"][1],
                                                    "dhuhr": day["vakat"][2],
                                                    "asr": day["vakat"][3],
                                                    "maghrib": day["vakat"][4],
                                                    "isha": day["vakat"][5]
                                                })
            result["success"] = True
            return result

        except Exception as e:
            print(e)
            return result

    def get_locations():
        """
        Returns the available locations.
        """
        try:
            file = open("app/static/vaktijaba_locations.json", "r")
            return json.load(file)
        except:
            try:
                # Send a request to the VaktijaEU API to get the locations
                return requests.get("https://api.vaktija.ba/vaktija/v1/lokacije").json()
            except:
                return None

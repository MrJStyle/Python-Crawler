import requests
from lxml import etree


def get_xpath(html):
    return etree.HTML(html)


header = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Content-Type": "application/json",
    "referer": "https://flights.ctrip.com/international/search/round-hkg-bkk?depdate=2019-10-01_2019-10-06&directflight=1&sort=price_asc&sourcepage=pricemap&sourcedata=%7B%22dCode%22%3A%22HKG%22%2C%22aCode%22%3A%22BKK%22%7D"
}

url = "https://flights.ctrip.com/international/search/api/flight/comfort/batchGetComfortTagList?v=0.1344767620565006"

data = [{"arrivalCityCode":"TPE","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["BR856"]},{"arrivalCityCode":"BKK","departureCityCode":"TPE","departureDate":"2019-10-01","flightNoList":["BR205"]},{"arrivalCityCode":"SIN","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["SQ001"]},{"arrivalCityCode":"BKK","departureCityCode":"SIN","departureDate":"2019-10-01","flightNoList":["SQ974"]},{"arrivalCityCode":"MNL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["PR301"]},{"arrivalCityCode":"BKK","departureCityCode":"MNL","departureDate":"2019-10-01","flightNoList":["PR736"]},{"arrivalCityCode":"MNL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["PR311"]},{"arrivalCityCode":"BKK","departureCityCode":"MNL","departureDate":"2019-10-02","flightNoList":["PR730"]},{"arrivalCityCode":"MNL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["PR319"]},{"arrivalCityCode":"BKK","departureCityCode":"MNL","departureDate":"2019-10-01","flightNoList":["PR732"]},{"arrivalCityCode":"MNL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["5J113"]},{"arrivalCityCode":"BKK","departureCityCode":"MNL","departureDate":"2019-10-02","flightNoList":["5J929"]},{"arrivalCityCode":"KUL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["MH073"]},{"arrivalCityCode":"BKK","departureCityCode":"KUL","departureDate":"2019-10-01","flightNoList":["MH796"]},{"arrivalCityCode":"KUL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["MH433"]},{"arrivalCityCode":"BKK","departureCityCode":"KUL","departureDate":"2019-10-02","flightNoList":["MH798"]},{"arrivalCityCode":"MNL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["5J113"]},{"arrivalCityCode":"BKK","departureCityCode":"MNL","departureDate":"2019-10-02","flightNoList":["5J931"]},{"arrivalCityCode":"TPE","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["CI928"]},{"arrivalCityCode":"BKK","departureCityCode":"TPE","departureDate":"2019-10-02","flightNoList":["CI833"]},{"arrivalCityCode":"TPE","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["BR872"]},{"arrivalCityCode":"BKK","departureCityCode":"TPE","departureDate":"2019-10-01","flightNoList":["BR061"]},{"arrivalCityCode":"TPE","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["BR810"]},{"arrivalCityCode":"BKK","departureCityCode":"TPE","departureDate":"2019-10-02","flightNoList":["BR201"]},{"arrivalCityCode":"MNL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["PR307"]},{"arrivalCityCode":"BKK","departureCityCode":"MNL","departureDate":"2019-10-02","flightNoList":["PR730"]},{"arrivalCityCode":"MNL","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["5J115"]},{"arrivalCityCode":"BKK","departureCityCode":"MNL","departureDate":"2019-10-02","flightNoList":["5J929"]},{"arrivalCityCode":"SIN","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["SQ857"]},{"arrivalCityCode":"BKK","departureCityCode":"SIN","departureDate":"2019-10-01","flightNoList":["SQ976"]},{"arrivalCityCode":"BKK","departureCityCode":"HKG","departureDate":"2019-10-01","flightNoList":["FD503","FD505","TG639","CX669","RJ183","CX617","TG601","TG603","CX751","TG607","HX767","HX765","CX701","CX703","HX761","CX705","WE631","UO702","CX717","CX755","HX779","HX775","CX653","EK385","TG629","FD509","CX727"]}]
import requests
from requests.exceptions import RequestException

class BookingService:
    def book(self, dto):
        
        payload = self._prepare_payload(dto)
        try:
            response = requests.post('/home/bookings/')
        except RequestException:
            raise 


    @staticmethod
    def _prepare_payload(dto):
        return
        {
            "event": dto.event,
            "member": dto.member
        }
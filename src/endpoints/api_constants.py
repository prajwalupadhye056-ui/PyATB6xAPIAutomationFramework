
#API Constants- Class which contains all the endpoints

#keep

#restfulbooker api, /booking ,booking/id ,/auth , /ping

class APIConstants:
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    #Update ->Put,Patch, Delete - bookingid

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)



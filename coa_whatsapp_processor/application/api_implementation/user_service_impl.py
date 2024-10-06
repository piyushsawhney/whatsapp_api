from coa_whatsapp_processor.api.user_service_api import IUserServiceApi


class UserServiceApi(IUserServiceApi):

    def get(self):
        return {"name":"loveyou"}

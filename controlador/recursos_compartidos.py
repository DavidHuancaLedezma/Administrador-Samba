class RecursosCompartidos():
    def __init__(self, status, read_only, name, path, guest_acces, comment):
        self.__status = status
        self.__read_only = read_only
        self.__name = name
        self.__path = path
        self.__guest_acces = guest_acces
        self.__comment = comment
    def get_status(self):
        return self.__status
    def get_read_only(self):
        return self.__read_only
    def get_name(self):
        return self.__name
    def get_path(self):
        return self.__path
    def get_guest_acces(self):
        return self.__guest_acces
    def get_comment(self):
        return self.__comment
    
    def set_status(self, status):
        self.__status = status
    def set_read_only(self, read_only):
        self.__read_only = read_only
    def set_name(self, name):
        self.__name = name
    def set_path(self, path):
        self.__path = path
    def set_guest_acces(self, guest_acces):
        self.__guest_acces = guest_acces
    def set_comment(self, comment):
        self.__comment = comment
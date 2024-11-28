class Settings:
    def __init__(self):
        self._mail_username = ""
        self._mail_password = ""
        self._mail_from = ""
        self._mail_port = ""
        self._mail_server = ""
        self._frontend_url = ""

    @property
    def mail_username(self):
        return self._mail_username

    @property
    def mail_password(self):
        return self._mail_password

    @property
    def mail_from(self):
        return self._mail_from

    @property
    def mail_port(self):
        return self._mail_port

    @property
    def mail_server(self):
        return self._mail_server

    @property
    def frontend_url(self):
        return self._frontend_url

    @property
    def settings(self):
        return [
            self._mail_username,
            self._mail_password,
            self._mail_from,
            self._mail_port,
            self._mail_server,
            self._frontend_url
        ]



class Config:
    def __init__(self, database, username, password, host, port, entorno):
        self.database = database
        self.username = username
        self.password = password
        self.host= host
        self.port = port
        self.entorno = entorno
    
    def __str__(self):
        return f"Se realizo la configuracion en el entorno de {self.entorno}"


class DataBaseConnect:
    def __init__(self, config: Config = None):
       self.config = config
    
    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        if isinstance(value, Config):
            self.__config = value
        else:
            raise ValueError("No se pudo realizar la Conexion")

    def __str__(self):
        if self.config:
            return "Conexion realizada con exito"


if __name__ == "__main__":
    # configuración para desarrollo, producción o testing
    development = Config('pywombat', 'root', 'password', 'localhost', 2207, 'development')
    production = Config('pywombat', 'superadmin', 'password', '157.245.120.121', 2207, 'production')
    testing= Config('pywombat', 'test', 'password', '157.245.120.121', 2207, 'testing')
    entornoCualquiera = "diseño"
    print(development)
    print(production)
    print(testing)

    # nos conectamos a los diferentes entornos
    print(DataBaseConnect(development))
    print(DataBaseConnect(production))
    print(DataBaseConnect(testing))
    print(DataBaseConnect(entornoCualquiera))

def coneccion_oracle_data_base (user_name,pasword_name,dns_path)
     """
	 Se crea la conexion a la base de datos oracle
	 :param user_name :Nombre de usuario
	 :param pasword_name :Contrasena de conexion
	 :param dns_path :Ruta DNS de la conexion
	 : retorna variable con la cadena de conexion
	 """
	 oracle_connection=cx_oracle.connect(user_name,pasword_name,dns_path)
	 return oracle_connection
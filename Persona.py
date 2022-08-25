class Persona:
    
    t_salida = 0
    t_llegada= 0    

    def __init__ (self, id, t_llegada):
        self.id = id
        self.t_llegada=t_llegada

        
    def set_t_salida(self, t_salida):
        self.t_salida=t_salida


    def __repr__(self):  
        #return "Persona:% i tiempo de llegada: % i tiempo de salida: " % (self.id, self.t_llegada,self.t_salida)
        return f'("id": {self.id},"entryTime": {self.t_llegada}, "outTime":{self.t_salida})'   

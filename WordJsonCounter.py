
from mrjob.job import MRJob
import json
import re

class WordJsonCounter(MRJob):

    # Función para extraer las palabras de las reseñas
    def mapper(self, _, line):
        try:
            # Obtenemos la línea de texto del json contenida en la clave 'review'
            review = json.loads(line).get('review', '')

            # Tokeniza la linea de reseña en palabras
            words = re.findall(r'\w+', review.lower())        

            # Añade el 1 como valor a cada palabra para contar las ocurrencias en el reduce
            for word in words:
                yield (word, 1)
       
        # Ignora los errores al leer el json
        except json.JSONDecodeError:
            pass  

    # Función para sumar las ocurrencias localmente en cada nodo
    def combiner(self, word, counts):
        yield (word, sum(counts))

    # Función para sumar todas las ocurrencias de una palabra
    def reducer(self, word, counts):
        yield (word, sum(counts))

# Función para ordenar las palabras por frecuencia de mayor a menor
def reducer_sorter(self, word, counts):

    # Creamos un diccionario para contar la frecuencia de las palabras
    word_count = dict(counts)
   
    # Ordena las palabras en función de su frecuencia en orden descendente.
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)  
   
    # Recorre la lista de palabras ordenadas y las emite como resultado.
    for word, count in sorted_words:
        yield (word, count)


    # Definimos el orden y q funciones ejecutar en el porcceso de MapReduce con la función steps()
    def steps(self):
        return [
            self.mr(mapper=self.mapper,
                    combiner=self.combiner,
                    reducer=self.reducer),
            self.mr(reducer=self.reducer_sorter)
        ]

if __name__ == '__main__':
    WordJsonCounter.run()


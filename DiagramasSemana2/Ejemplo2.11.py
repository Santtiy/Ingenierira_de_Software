#Ejemplo2.11
def calcularMetrosCubicos(ancho, largo, profundidad):
    precioMetroCubico = 5600
    
    volumenAlberca = ancho*largo*profundidad
    TotalAPagar = volumenAlberca*precioMetroCubico
    return TotalAPagar

print(calcularMetrosCubicos)
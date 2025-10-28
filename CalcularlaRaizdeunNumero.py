
import math

def calcular_raiz_cuadrada(numero):
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo en el conjunto de los números reales."
    else:
        # Usa la función sqrt() del módulo math
        return math.sqrt(numero)

def main():
    print("--- Calculadora de Raíz Cuadrada ---")
    
    while True:
        entrada = input("Ingresa un número (o 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break

        try:
            # Intenta convertir la entrada a un número flotante
            numero = float(entrada)
            
            # Llama a la función de cálculo
            resultado = calcular_raiz_cuadrada(numero)
            
            # Imprime el resultado
            if isinstance(resultado, str):
                # Si es un mensaje de error
                print(resultado)
            else:
                # Si es un resultado numérico
                print(f"La raíz cuadrada de {numero} es: {resultado:.4f}") # Formato a 4 decimales
                
        except ValueError:
            # Captura errores si la entrada no es un número válido
            print("Entrada no válida. Por favor, ingresa un número o escribe 'salir'.")

if __name__ == "__main__":
    main()
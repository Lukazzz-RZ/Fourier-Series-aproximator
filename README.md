# Fourier-Series-aproximator

## Introducción (ES)

Este proyecto aborda la resolución numérica de problemas relacionados con ondas electromagnéticas, incluyendo la representación gráfica de la respuesta en frecuencia y el análisis de desarrollos en series de Fourier para trenes de pulsos gaussianos. 

---

## Representación gráfica de la respuesta en frecuencia

### Observaciones:
- Para un período fijo, cuanto menor es la anchura de la gaussiana, menor es la respuesta en frecuencia para un armónico dado.
- En el caso de \(m = 0\), la respuesta en frecuencia está determinada únicamente por el coeficiente de reducción de anchura del medio (\(n\)).

### Gráficos:
Se han representado las respuestas en frecuencia frente al número de armónicos para diferentes valores del cociente \(P/\Delta t\), mostrando cómo varían los resultados en función de los parámetros del sistema.

---

## Desarrollo en serie de Fourier

Se utilizó Python para determinar la cantidad de términos necesarios para representar un tren de pulsos gaussianos mediante un desarrollo en serie de Fourier. La comparación se realizó tomando un período fijo y variando la anchura de la gaussiana.

### Observaciones:
1. Cuanto menor es la anchura de la gaussiana, mayor será el número de términos necesarios para una aproximación correcta.
2. La similitud entre la función original y su serie de Fourier comienza a ser notable alrededor de \(m \approx P / (2 \cdot \Delta t)\).

### Resultados:
| \(P/\Delta t\) | Número de términos necesarios para aproximación correcta |
|----------------|--------------------------------------------------------|
| 10            | 5                                                      |
| 20            | 10                                                     |
| 30            | 15                                                     |
| 40            | 20                                                     |
| 50            | 25                                                     |

#### Conclusión:
El número de términos necesarios para una aproximación correcta es independiente del período mientras se mantenga constante el cociente entre el período y la anchura de la gaussiana (\(P / \Delta t\)).

---

## Ilustraciones

### Ejemplo de pulsos gaussianos:
1. Pulso gaussiano para \(P/\Delta t = 10\)
2. Pulso gaussiano para \(P/\Delta t = 20\)
3. Pulso gaussiano para \(P/\Delta t = 50\)

---

## Conclusión

Se ha demostrado que la relación \(m \approx P / (2 \cdot \Delta t)\) es válida para obtener una aproximación adecuada en desarrollos de series de Fourier de trenes de pulsos gaussianos, especialmente bajo la condición \(\Delta t \ll P\). Este análisis proporciona una herramienta útil para estudiar fenómenos relacionados con la respuesta en frecuencia de sistemas electromagnéticos y sus aproximaciones mediante series de Fourier.

# Grupo 6: Algoritmo Diferencial

Implementación de un algoritmo diferencial

## Integrantes:
*   Luis Fernando Moya Lozada
*   Jesús Jerez Ballesteros
*   Qi Ye

## Estructura:
* HeuristicOP
  * __init__.py
  * LICENSE
  * Prueba.py
  * README.md
  * setup.py
  * group06
    * EA.py
    * Genome.py
    * Population.py
    * SeleccionOperator.py
    * MutationOperator.py
    * CrossoverOperator.py
    * ReplacementOperator.py
    * operadores
      * Uniform.py
      * CurrentToRand.py
      * Arithmetic.py
      * Elitist.py

<br> <br/>
## Operadores especificos:
*   CrossoverOperator: Se ha utilizado un operador de cruce **aritmético**, que genera una nueva solución realizando la combinación lineal entre dos individuos.
  
* MutationOperator: Se ha implementado el operador de mutación usando el modelo **de/current to rand/1**, que genera un vector mutante formado a partir de la combinacion del target vector y otros tres vectores aleatorios.


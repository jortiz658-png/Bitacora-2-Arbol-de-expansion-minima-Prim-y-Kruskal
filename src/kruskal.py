"""
Módulo: kruskal.py
Algoritmo de Kruskal con Union-Find.
Complejidad: O(E log E) tiempo, O(V + E) espacio.

Equipo 5 – Análisis y Diseño de Algoritmos – UNEG
Integrantes:
  - Ing. Bryan Salazar
  - Ing. Johana Carvajal
  - Ing. David González
  - Ing. Yrene Corrales
  - Ing. José Ortiz
"""

from __future__ import annotations

from grafo import Grafo
from prim import ResultadoMST
from union_find import UnionFind


def kruskal(grafo: Grafo) -> ResultadoMST:
    """
    Calcula el Árbol de Expansión Mínima (o Bosque de Expansión Mínima si el
    grafo es disconexo) mediante el algoritmo de Kruskal con Union-Find.

    Complejidad temporal: O(E log E), dominada por el ordenamiento de aristas.
    Complejidad espacial: O(V + E).

    Args:
        grafo: Grafo no dirigido y ponderado con pesos no negativos.

    Returns:
        ResultadoMST con las aristas seleccionadas y el peso total acumulado.
    """
    n = grafo.n_vertices
    resultado = ResultadoMST()

    if n == 0:
        return resultado

    # grafo.aristas() retorna tuplas (w, u, v), por lo que sorted() ordena por peso
    aristas_ordenadas = sorted(grafo.aristas())
    uf = UnionFind(n)

    for w, u, v in aristas_ordenadas:
        # Solo se agrega la arista si u y v pertenecen a componentes disjuntas
        if uf.unir(u, v):
            resultado.agregar(u, v, w)
            if len(resultado.aristas_mst) == n - 1:
                break

    return resultado

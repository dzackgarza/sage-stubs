from sage.manifolds.chart import Chart
from sage.manifolds.manifold import TopologicalManifold
from sage.manifolds.scalarfield_algebra import ScalarFieldAlgebra
from sage.categories.category import Category

class TopologicalStructure:
    name: str
    chart: type[Chart]
    def subcategory(self, category: Category) -> Category: ...
    def scalar_field_algebra(self, domain: TopologicalManifold) -> ScalarFieldAlgebra: ...

class RealTopologicalStructure(TopologicalStructure):
    ...

class DifferentialStructure(TopologicalStructure):
    ...

class RealDifferentialStructure(DifferentialStructure, RealTopologicalStructure):
    ...

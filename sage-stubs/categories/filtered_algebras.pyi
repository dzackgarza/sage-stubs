from sage.categories.filtered_modules import FilteredModulesCategory
from sage.structure.parent import Parent

class FilteredAlgebras(FilteredModulesCategory):
    class ParentMethods:
        def graded_algebra(self) -> Parent: ...

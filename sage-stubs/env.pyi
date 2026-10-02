# Generated from the pinned Sage 10.7 source tree.
from collections.abc import Iterable

# env.py:34: ``var`` records in ``SAGE_ENV`` each value it returns.
SAGE_ENV: dict[str, str | None]

def join(*args: str | None) -> str | None: ...
def var(key: str, *fallbacks: str | None, force: bool = False) -> str | None: ...

# Each constant is ``var(...)`` (env.py:145-242), whose value is ``None`` when
# the variable is unset and every fallback is ``None``; ``SINGULAR_BIN`` is
# ``var(...) or "Singular"``.
HOSTNAME: str | None
LOCAL_IDENTIFIER: str | None
SAGE_VERSION: str | None
SAGE_DATE: str | None
SAGE_VERSION_BANNER: str | None
SAGE_LIB: str | None
SAGE_EXTCODE: str | None
SAGE_LOCAL: str | None
SAGE_SHARE: str | None
SAGE_DOC: str | None
SAGE_LOCAL_SPKG_INST: str | None
SAGE_SPKG_INST: str | None
SAGE_ROOT: str | None
SAGE_SRC: str | None
SAGE_DOC_SRC: str | None
SAGE_PKGS: str | None
SAGE_ROOT_GIT: str | None
SAGE_DOC_SERVER_URL: str | None
SAGE_DOC_LOCAL_PORT: str | None
DOT_SAGE: str | None
SAGE_STARTUP_FILE: str | None
SAGE_ARCHFLAGS: str | None
SAGE_PKG_CONFIG_PATH: str | None
SAGE_DATA_PATH: str | None
CREMONA_LARGE_DATA_DIR: str | None
CREMONA_MINI_DATA_DIR: str | None
ELLCURVE_DATA_DIR: str | None
GRAPHS_DATA_DIR: str | None
POLYTOPE_DATA_DIR: str | None
JMOL_DIR: str | None
MATHJAX_DIR: str | None
MTXLIB: str | None
THREEJS_DIR: str | None
PPLPY_DOCS: str | None
MAXIMA: str | None
MAXIMA_FAS: str | None
MAXIMA_PREFIX: str | None
KENZO_FAS: str | None
SAGE_NAUTY_BINS_PREFIX: str | None
SAGE_ECMBIN: str | None
RUBIKS_BINS_PREFIX: str | None
FOURTITWO_HILBERT: str | None
FOURTITWO_MARKOV: str | None
FOURTITWO_GRAVER: str | None
FOURTITWO_ZSOLVE: str | None
FOURTITWO_QSOLVE: str | None
FOURTITWO_RAYS: str | None
FOURTITWO_PPI: str | None
FOURTITWO_CIRCUITS: str | None
FOURTITWO_GROEBNER: str | None
ECL_CONFIG: str | None
NTL_INCDIR: str | None
NTL_LIBDIR: str | None
LIE_INFO_DIR: str | None
SINGULAR_BIN: str
OPENMP_CFLAGS: str | None
OPENMP_CXXFLAGS: str | None
SAGE_BANNER: str | None
SAGE_IMPORTALL: str | None
SAGE_GAP_MEMORY: str | None
SAGE_GAP_COMMAND: str | None

def sage_include_directories(use_sources: bool = False) -> list[str]: ...

default_required_modules: tuple[str, ...]
default_optional_modules: tuple[str, ...]

def cython_aliases(
    required_modules: Iterable[str] | None = None,
    optional_modules: Iterable[str] | None = None,
) -> dict[str, str | list[str]]: ...
def sage_data_paths(name: str = "") -> set[str]: ...

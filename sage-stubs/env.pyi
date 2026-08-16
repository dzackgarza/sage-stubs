import builtins

class _SageObject: ...

SAGE_ENV: _SageObject

def join(self, *args: builtins.object) -> str | None: ...
def var(
    self, *fallbacks: builtins.object, force: builtins.bool = ...
) -> str | None: ...

HOSTNAME: _SageObject
LOCAL_IDENTIFIER: _SageObject
SAGE_VERSION: _SageObject
SAGE_DATE: _SageObject
SAGE_VERSION_BANNER: _SageObject
SAGE_LIB: _SageObject
SAGE_EXTCODE: _SageObject
SAGE_LOCAL: _SageObject
SAGE_SHARE: _SageObject
SAGE_DOC: _SageObject
SAGE_LOCAL_SPKG_INST: _SageObject
SAGE_SPKG_INST: _SageObject
SAGE_ROOT: _SageObject
SAGE_SRC: _SageObject
SAGE_DOC_SRC: _SageObject
SAGE_PKGS: _SageObject
SAGE_ROOT_GIT: _SageObject
SAGE_DOC_SERVER_URL: _SageObject
SAGE_DOC_LOCAL_PORT: _SageObject
DOT_SAGE: _SageObject
SAGE_STARTUP_FILE: _SageObject
SAGE_ARCHFLAGS: _SageObject
SAGE_PKG_CONFIG_PATH: _SageObject
SAGE_DATA_PATH: _SageObject
CREMONA_LARGE_DATA_DIR: _SageObject
CREMONA_MINI_DATA_DIR: _SageObject
ELLCURVE_DATA_DIR: _SageObject
GRAPHS_DATA_DIR: _SageObject
POLYTOPE_DATA_DIR: _SageObject
JMOL_DIR: _SageObject
MATHJAX_DIR: _SageObject
MTXLIB: _SageObject
THREEJS_DIR: _SageObject
PPLPY_DOCS: _SageObject
MAXIMA: _SageObject
MAXIMA_FAS: _SageObject
MAXIMA_PREFIX: _SageObject
KENZO_FAS: _SageObject
SAGE_NAUTY_BINS_PREFIX: _SageObject
SAGE_ECMBIN: _SageObject
RUBIKS_BINS_PREFIX: _SageObject
FOURTITWO_HILBERT: _SageObject
FOURTITWO_MARKOV: _SageObject
FOURTITWO_GRAVER: _SageObject
FOURTITWO_ZSOLVE: _SageObject
FOURTITWO_QSOLVE: _SageObject
FOURTITWO_RAYS: _SageObject
FOURTITWO_PPI: _SageObject
FOURTITWO_CIRCUITS: _SageObject
FOURTITWO_GROEBNER: _SageObject
ECL_CONFIG: _SageObject
NTL_INCDIR: _SageObject
NTL_LIBDIR: _SageObject
LIE_INFO_DIR: _SageObject
SINGULAR_BIN: _SageObject
OPENMP_CFLAGS: _SageObject
OPENMP_CXXFLAGS: _SageObject
SAGE_BANNER: _SageObject
SAGE_IMPORTALL: _SageObject
SAGE_GAP_MEMORY: _SageObject
SAGE_GAP_COMMAND: _SageObject

def sage_include_directories(self=...) -> _SageObject: ...

default_required_modules: _SageObject
default_optional_modules: _SageObject

def cython_aliases(
    self=..., optional_modules: builtins.object = ...
) -> _SageObject: ...
def sage_data_paths(self=...) -> set[str]: ...

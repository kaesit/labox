from setuptools import setup, Extension
import pybind11

ext_modules = [
        Extension(
            "labox_embedded_core",
            ["source/bindings.cpp"],
            include_dirs = [pybind11.get_include()],
            language = "c++",
            extra_compile_args = ["-std=c++17", "-O3"]
        ),
]

setup(
        name = "labox_embedded",
        ext_modules=ext_modules,
)

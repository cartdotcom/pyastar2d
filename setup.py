import setuptools
from distutils.core import Extension
import numpy

astar_module = Extension(
    'pyastar2d.astar', sources=['src/cpp/astar.cpp', 'src/cpp/experimental_heuristics.cpp'],
    include_dirs=[
                    numpy.get_include(),   # for numpy/arrayobject.h
                    'src/cpp'    # for experimental_heuristics.h
                 ],
    extra_compile_args=["-O3", "-Wall", "-shared", "-fpic"],
)

setuptools.setup(
    # name="cartastar2d",
    # version="0.1.0",
    # packages=setuptools.find_packages(where="src", exclude=("tests",)),
    # package_dir={"": "src"},
    ext_modules=[astar_module],
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # python_requires='>=3.7',
)

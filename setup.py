from setuptools import setup
setup(
    name = 'vr2p',
    version = '1.0.0',
    description = 'Tools for analyzing VR and suite2p data',
    url = 'https://github.com/winnubstj/vr2p',
    author = 'Johan Winnubst',
    author_email = 'https://github.com/sprustonlab/vr2p',
    packages = ['vr2p'],
    zip_safe = False
    install_requires=[
        # Core numerical stack (explicit pins from environment.yml)
        "numpy==1.22.1",
        "pandas==1.4.0",
        "scipy",
        "numba",
    
        # Imaging / ML
        "scikit-image",
        "scikit-learn",
        "matplotlib",
    
        # IO / storage
        "h5py",
        "pyyaml",
        "gcsfs",
        "zarr==2.8.1",
    
        # Utilities
        "colorcet",
        "ipyfilechooser",
    
        # Pip-only dependency (explicitly newer than conda)
        "pirt==2.1.0",
    ],
    extras_require={
        "jupyter": [
            "jupyterlab",
            "ipympl",
        ],
        "napari": [
            "napari[all]",
        ],
        "dev": [
            "pytest",
            "black",
            "ruff",
            "mypy",
        ],
    },
)

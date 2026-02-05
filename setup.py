from setuptools import setup
setup(
    name = 'vr2p',
    version = '1.0.0',
    description = 'Tools for analyzing VR and suite2p data',
    url = 'https://github.com/winnubstj/vr2p',
    author = 'Johan Winnubst',
    author_email = 'https://github.com/sprustonlab/vr2p',
    packages = ['vr2p'],
    zip_safe = False,
    install_requires=[
        # Core numerical stack (explicit pins from environment.yml)
        "numpy < 2",
        "pandas",
        "scipy",
        "numba",
        "tqdm",
    
        # Imaging / ML
        "scikit-image",
        "scikit-learn",
        "matplotlib",
    
        # IO / storage
        "h5py",
        "pyyaml",
        "gcsfs",
        "zarr < 3",
    
        # Utilities
        "colorcet",
        "ipyfilechooser",
    
        # Pip-only dependency (explicitly newer than conda)
        "pirt",
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

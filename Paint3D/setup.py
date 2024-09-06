from setuptools import setup, find_packages

setup(
    name="paint3d",  # Replace with your package name
    version="0.1.0",  # Replace with your package version
    description="A 3D painting tool",  # Replace with a brief description of your project
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    url="https://github.com/yourusername/paint3d",  # Replace with your project's URL if available
    packages=find_packages(),  # Automatically find packages in the directory
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=[
        # List your project's dependencies here, e.g., 'numpy', 'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            # Add command-line scripts here, e.g., 'paint3d=paint3d:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
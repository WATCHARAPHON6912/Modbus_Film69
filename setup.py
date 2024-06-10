from setuptools import setup, find_packages

setup(
    name="Modbus_Film69",
    version="0.0.1",
    description="A Modbus communication module for Film69 devices",
    py_modules=["ModbusFilm69"],
    install_requires=[
        "pyserial",
        "minimalmodbus",
    ],
    entry_points={
        'console_scripts': [
            'ModbusFilm69=modbusFilm69:Modbus_Film69',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

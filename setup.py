from setuptools import setup, find_packages

setup(
    name="modbus_film69",
    version="0.0.2",
    description="A Modbus communication module for Film69 devices",
    py_modules=["Modbus_Film69"],  # ต้องตรงกับชื่อไฟล์ Modbus_Film69.py
    install_requires=[
        "pyserial",
        "minimalmodbus",
    ],
    entry_points={
        'console_scripts': [
            'modbus_film69=Modbus_Film69:Modbus_Film69',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

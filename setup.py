"""Setup module for zigpy-zigate"""

import pathlib
import zigpy_zigate

from setuptools import find_packages, setup


def get_hardware_name() -> str:
    """
    Reads the hardware name from /proc/cpuinfo. If there is an error, the empty string
    is returned.
    """
    try:
        with open("/proc/cpuinfo", "r") as cpuinfo:
            for line in cpuinfo:
                if line.startswith("Hardware"):
                    return line.split(":", 1)[1].strip()
    except IOError:
        pass

    return ""


requires = [
    'pyserial>=3.5',
    'pyserial-asyncio; platform_system!="Windows"',
    'pyserial-asyncio!=0.5; platform_system=="Windows"',  # 0.5 broke writes
    'zigpy>=0.22.2',
]


hardware = get_hardware_name()

if hardware in ("BCM2708", "BCM2709", "BCM2835", "BCM2836"):
    requires.append("RPi.GPIO")
elif hardware.startswith("ODROID"):
    requires.append("Odroid.GPIO")


setup(
    name="zigpy-zigate",
    version=zigpy_zigate.__version__,
    description="A library which communicates with ZiGate radios for zigpy",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="http://github.com/zigpy/zigpy-zigate",
    author="Sébastien RAMAGE",
    author_email="sebatien.ramage@gmail.com",
    license="GPL-3.0",
    packages=find_packages(exclude=['tests']),
    install_requires=requires,
    tests_require=[
        'pytest',
        'pytest-asyncio',
        'mock'
    ],
)

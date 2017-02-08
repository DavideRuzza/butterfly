# coding=utf-8
"""Versions and header."""
from copy import deepcopy
from datetime import datetime


class Version(object):
    """Version class."""

    BFVer = "0.0.3"
    OFVer = "3.0"
    OFFullVer = "v1612+"
    isUsingDockerMachine = True  # useful to run OpenFOAM container
    lastUpdated = datetime(year=2017, month=2, day=7, hour=9, minute=00)

    def duplicate(self):
        """Return a copy of this object."""
        return deepcopy(self)

    def ToString(self):
        """Overwrite .NET ToString method."""
        return self.__repr__()

    def __repr__(self):
        """Version."""
        return 'Version::Butterfly{}::OpenFOAM{}'.format(self.BFVer, self.OFVer)


class Header(object):
    """Input files header.

    Usage:
        Header.header()
    """

    @staticmethod
    def header(OpenFOAMVersion=Version.OFFullVer, ButterflyVersion=Version.BFVer):
        """Retuen OpenFOAM file header."""
        header = \
            "/*--------------------------------*- C++ -*----------------------------------*\\\n" + \
            "| =========                 |                                                 |\n" + \
            "| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n" + \
            "|  \\\\    /   O peration     | Version:  {}                                |\n" + \
            "|   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |\n" + \
            "|    \\\\/     M anipulation  |                                                 |\n" + \
            "\\*---------------------------------------------------------------------------*/\n" + \
            "/* Butterfly {}       https://github.com/ladybug-analysis-tools/butterfly *\\\n" + \
            "\\*---------------------------------------------------------------------------*/\n"

        return header.format(OpenFOAMVersion, ButterflyVersion)

    def duplicate(self):
        """Return a copy of this object."""
        return deepcopy(self)

    def ToString(self):
        """Overwrite .NET ToString method."""
        return self.__repr__()

    def __repr__(self):
        """Header."""
        return self.header

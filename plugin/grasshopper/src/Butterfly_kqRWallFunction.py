# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
kqRWallFunction boundary condition.

-
    Args:
        _value: input value.
        
    Returns:
        kqRWallFunction: kqRWallFunction boundary condition.
"""

ghenv.Component.Name = "Butterfly_kqRWallFunction"
ghenv.Component.NickName = "kqRWallFunction"
ghenv.Component.Message = 'VER 0.0.03\nFEB_20_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "02::BoundaryCondition"
ghenv.Component.AdditionalHelpFromDocStrings = "1"


try:
    from butterfly.fields import KqRWallFunction
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/grasshopper/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))    

if _value:
    kqRWallFunction = KqRWallFunction(_value)
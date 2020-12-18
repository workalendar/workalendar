from unittest import TestCase
from ..usa import (
    UnitedStates,
    Alabama,
    Alaska,
    Arizona,
    Arkansas,
    California,
    Colorado,
    Connecticut,
    Delaware,
    DistrictOfColumbia,
    Florida,
    Georgia,
    Hawaii,
    Idaho,
    Illinois,
    Indiana,
    Iowa,
    Kansas,
    Kentucky,
    Louisiana,
    Maine,
    Maryland,
    Massachusetts,
    Michigan,
    Minnesota,
    Mississippi,
    Missouri,
    Montana,
    Nebraska,
    Nevada,
    NewHampshire,
    NewJersey,
    NewMexico,
    NewYork,
    NorthCarolina,
    NorthDakota,
    Ohio,
    Oklahoma,
    Oregon,
    Pennsylvania,
    RhodeIsland,
    SouthCarolina,
    SouthDakota,
    Tennessee,
    Texas,
    Utah,
    Vermont,
    Virginia,
    Washington,
    WestVirginia,
    Wisconsin,
    Wyoming
)

from ..registry import registry


class RegistryUsa(TestCase):

    def _check_all_states(self, classes):
        self.assertIn(Alabama, classes)
        self.assertIn(Alaska, classes)
        self.assertIn(Arizona, classes)
        self.assertIn(Arkansas, classes)
        self.assertIn(California, classes)
        self.assertIn(Colorado, classes)
        self.assertIn(Connecticut, classes)
        self.assertIn(Delaware, classes)
        self.assertIn(DistrictOfColumbia, classes)
        self.assertIn(Florida, classes)
        self.assertIn(Georgia, classes)
        self.assertIn(Hawaii, classes)
        self.assertIn(Idaho, classes)
        self.assertIn(Illinois, classes)
        self.assertIn(Indiana, classes)
        self.assertIn(Iowa, classes)
        self.assertIn(Kansas, classes)
        self.assertIn(Kentucky, classes)
        self.assertIn(Louisiana, classes)
        self.assertIn(Maine, classes)
        self.assertIn(Maryland, classes)
        self.assertIn(Massachusetts, classes)
        self.assertIn(Michigan, classes)
        self.assertIn(Minnesota, classes)
        self.assertIn(Mississippi, classes)
        self.assertIn(Missouri, classes)
        self.assertIn(Montana, classes)
        self.assertIn(Nebraska, classes)
        self.assertIn(Nevada, classes)
        self.assertIn(NewHampshire, classes)
        self.assertIn(NewJersey, classes)
        self.assertIn(NewMexico, classes)
        self.assertIn(NewYork, classes)
        self.assertIn(NorthCarolina, classes)
        self.assertIn(NorthDakota, classes)
        self.assertIn(Ohio, classes)
        self.assertIn(Oklahoma, classes)
        self.assertIn(Oregon, classes)
        self.assertIn(Pennsylvania, classes)
        self.assertIn(RhodeIsland, classes)
        self.assertIn(SouthCarolina, classes)
        self.assertIn(SouthDakota, classes)
        self.assertIn(Tennessee, classes)
        self.assertIn(Texas, classes)
        self.assertIn(Utah, classes)
        self.assertIn(Vermont, classes)
        self.assertIn(Virginia, classes)
        self.assertIn(Washington, classes)
        self.assertIn(WestVirginia, classes)
        self.assertIn(Wisconsin, classes)
        self.assertIn(Wyoming, classes)

    def test_usa_world(self):
        classes = set(registry.region_registry.values())
        self._check_all_states(classes)
        # On top of it, the core class
        self.assertIn(UnitedStates, classes)

    def test_usa_subregion(self):
        # Get all the subregions
        classes = set(registry.get_subregions('US').values())
        self._check_all_states(classes)

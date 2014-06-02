from unittest import TestCase
import ephem

class GitHubIssues(TestCase):

    def test_github_14(self):
        iss = ephem.readtle(
            'ISS (ZARYA)',
            '1 25544U 98067A   03097.78853147  .00021906 '
            ' 00000-0  28403-3 0  8652',
            '2 25544  51.6361  13.7980 0004256  35.6671  '
            '59.2566 15.58778559250029',
            )
        gatech = ephem.Observer()
        gatech.lon, gatech.lat = '-84.39733', '33.775867'
        gatech.date = '2003/3/23'
        iss.compute(gatech)
        self.assertEqual(str(iss.a_ra), '8:50:10.99')
        self.assertEqual(str(iss.g_ra), '6:54:40.64')
        self.assertEqual(str(iss.ra), '8:50:16.76')

    def test_github_31(self):
        position = (4.116325133165859, 0.14032240860186646)
        self.assertEqual(ephem.separation(position, position), 0.0)

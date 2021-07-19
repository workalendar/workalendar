import datetime
import json
import pathlib
from unittest import TestCase
from unittest.mock import MagicMock, call, patch, sentinel

from freezegun import freeze_time

from .. import precomputed_astronomy as mod


class PreComputedAstronomyTest(TestCase):
    def test_year_interval(self):
        self.assertEqual(mod.YEAR_INTERVAL, 30)

    def test_time_zones(self):
        self.assertEqual(mod.TIME_ZONES, (
            'America/Santiago',
            'Asia/Hong_Kong',
            'Asia/Taipei',
            'Asia/Tokyo',
        ))

    def test_pre_computed_pathes(self):
        self.assertEqual(
            mod.pre_computed_equinoxes_path,
            pathlib.Path(__file__).parent.parent / 'equinoxes.json.gz',
        )
        self.assertEqual(
            mod.pre_computed_solar_terms_path,
            pathlib.Path(__file__).parent.parent / 'solar_terms.json.gz',
        )

    @patch('workalendar.skyfield_astronomy.solar_term')
    @patch('workalendar.skyfield_astronomy.calculate_equinoxes')
    @patch('workalendar.precomputed_astronomy.gzip.open')
    @patch('workalendar.precomputed_astronomy.YEAR_INTERVAL', 1)
    @patch('workalendar.precomputed_astronomy.TIME_ZONES', ('Europe/Paris',))
    @freeze_time('2022-01-01')
    def test_create_astronomical_data(self,
                                      gzipopen,
                                      calculate_equinoxes,
                                      solar_term):
        equinoxes_file = MagicMock(name='equinoxes')
        equinoxes_file.__enter__.return_value = equinoxes_file
        solar_terms_file = MagicMock(name='solar_terms')
        solar_terms_file.__enter__.return_value = solar_terms_file
        gzipopen.side_effect = [equinoxes_file, solar_terms_file]
        calculate_equinoxes.side_effect = lambda year, timezone: (
            datetime.date(year=year, month=2, day=15),
            datetime.date(year=year, month=3, day=16),
        )
        solar_term.side_effect = lambda year, degrees, timezone: \
            datetime.date(year=year, month=7, day=21)
        mod.create_astronomical_data()
        gzipopen.assert_has_calls([
            call(mod.pre_computed_equinoxes_path, 'wb'),
            call(mod.pre_computed_solar_terms_path, 'wb'),
        ], any_order=True)
        expected_equinoxes_dict = {
            'Europe/Paris': {
                '2021': ('2021-02-15', '2021-03-16'),
                '2022': ('2022-02-15', '2022-03-16'),
                '2023': ('2023-02-15', '2023-03-16'),
            }
        }
        equinoxes_file.write.assert_called_once_with(
            json.dumps(expected_equinoxes_dict).encode('utf-8')
        )
        expected_solar_terms_dict = {
            'Europe/Paris': {
                '2021': {str(i): '2021-07-21' for i in range(15, 360, 15)},
                '2022': {str(i): '2022-07-21' for i in range(15, 360, 15)},
                '2023': {str(i): '2023-07-21' for i in range(15, 360, 15)},
            }
        }
        solar_terms_file.write.assert_called_once_with(
            json.dumps(expected_solar_terms_dict).encode('utf-8')
        )

    @patch('workalendar.precomputed_astronomy.gzip.decompress')
    @patch('workalendar.precomputed_astronomy.pre_computed_equinoxes_path')
    def test_calculate_equinoxes(self,
                                 pre_computed_equinoxes_path,
                                 decompress):
        pre_computed_equinoxes_path.read_bytes.return_value = \
            sentinel.some_equinoxes_bytes
        decompress.return_value = json.dumps({
            'Europe/Paris': {
                '2021': ('2021-02-15', '2021-03-16'),
                '2022': ('2022-02-15', '2022-03-16'),
                '2023': ('2023-02-15', '2023-03-16'),
            }
        }).encode('utf-8')
        with self.assertRaises(NotImplementedError):
            mod.calculate_equinoxes(2100, 'Europe/Paris')
        pre_computed_equinoxes_path.read_bytes.assert_called_once()
        pre_computed_equinoxes_path.reset_mock()
        decompress.assert_called_once_with(sentinel.some_equinoxes_bytes)
        decompress.reset_mock()
        with self.assertRaises(NotImplementedError):
            mod.calculate_equinoxes(2022, 'Europe/Berlin')
        pre_computed_equinoxes_path.read_bytes.assert_called_once()
        pre_computed_equinoxes_path.reset_mock()
        decompress.assert_called_once_with(sentinel.some_equinoxes_bytes)
        decompress.reset_mock()
        self.assertEqual(mod.calculate_equinoxes(2022, 'Europe/Paris'), (
            datetime.date(year=2022, month=2, day=15),
            datetime.date(year=2022, month=3, day=16),
        ))
        pre_computed_equinoxes_path.read_bytes.assert_called_once()
        pre_computed_equinoxes_path.reset_mock()
        decompress.assert_called_once_with(sentinel.some_equinoxes_bytes)
        decompress.reset_mock()

    @patch('workalendar.precomputed_astronomy.gzip.decompress')
    @patch('workalendar.precomputed_astronomy.pre_computed_solar_terms_path')
    def test_sorted_term(self,
                         pre_computed_solar_terms_path,
                         decompress):
        pre_computed_solar_terms_path.read_bytes.return_value = \
            sentinel.some_solar_terms_bytes
        decompress.return_value = json.dumps({
            'Europe/Paris': {
                '2021': {str(i): '2021-07-21' for i in range(15, 360, 15)},
                '2022': {str(i): '2022-07-21' for i in range(15, 360, 15)},
                '2023': {str(i): '2023-07-21' for i in range(15, 360, 15)},
            }
        }).encode('utf-8')
        with self.assertRaises(ValueError):
            mod.solar_term(2022, 0, 'Europe/Paris')
        with self.assertRaises(ValueError):
            mod.solar_term(2022, 360, 'Europe/Paris')
        with self.assertRaises(ValueError):
            mod.solar_term(2022, 20, 'Europe/Paris')
        with self.assertRaises(NotImplementedError):
            mod.solar_term(2100, 45, 'Europe/Paris')
        pre_computed_solar_terms_path.read_bytes.assert_called_once()
        pre_computed_solar_terms_path.reset_mock()
        decompress.assert_called_once_with(sentinel.some_solar_terms_bytes)
        decompress.reset_mock()
        with self.assertRaises(NotImplementedError):
            mod.solar_term(2022, 90, 'Europe/Berlin')
        pre_computed_solar_terms_path.read_bytes.assert_called_once()
        pre_computed_solar_terms_path.reset_mock()
        decompress.assert_called_once_with(sentinel.some_solar_terms_bytes)
        decompress.reset_mock()
        self.assertEqual(
            mod.solar_term(2022, 90, 'Europe/Paris'),
            datetime.date(year=2022, month=7, day=21),
        )
        pre_computed_solar_terms_path.read_bytes.assert_called_once()
        pre_computed_solar_terms_path.reset_mock()
        decompress.assert_called_once_with(sentinel.some_solar_terms_bytes)
        decompress.reset_mock()

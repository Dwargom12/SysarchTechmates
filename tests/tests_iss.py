import unittest
from iss_tracker import get_iss_location

class TestISS(unittest.TestCase):
    def test_location_format(self):
        lat, lon = get_iss_location()
        self.assertIsInstance(lat, float)
        self.assertIsInstance(lon, float)

if __name__ == "__main__":
    unittest.main()

    # cd path/to/iss-tracker

    # git init

    # git add .

    # git commit -m "Added Comments for Testing of Auto Debugger"

    # git branch -M main

    # git push -u origin main
import unittest
from star_system import StarSystem


class TestStarSystem(unittest.TestCase):
    def test_valid_creation_and_properties(self):
        s = StarSystem("Sol", "Yellow dwarf", "Single", 8, (0.95, 1.37))
        self.assertEqual(s.name, "Sol")
        self.assertEqual(s.star_type, "Yellow dwarf")
        self.assertEqual(s.system_type, "Single")
        self.assertEqual(s.num_planets, 8)
        self.assertEqual(s.habitable_zone_range, (0.95, 1.37))
        self.assertTrue(s.is_habitable)

    def test_name_validation_empty(self):
        with self.assertRaises(ValueError):
            StarSystem("   ", "Yellow dwarf", "Single", 1)

    def test_star_type_validation_invalid(self):
        with self.assertRaises(ValueError):
            StarSystem("Alpha", "Supernova", "Single", 1)

    def test_system_type_validation_invalid(self):
        with self.assertRaises(ValueError):
            StarSystem("Alpha", "Red dwarf", "Quadruple", 1)

    def test_num_planets_negative(self):
        with self.assertRaises(ValueError):
            StarSystem("Alpha", "Red dwarf", "Single", -3)

    def test_habitable_zone_invalid_length(self):
        with self.assertRaises(ValueError):
            StarSystem("Alpha", "Red dwarf", "Single", 1, (1,))

    def test_habitable_zone_start_greater_equal_end(self):
        with self.assertRaises(ValueError):
            StarSystem("Alpha", "Red dwarf", "Single", 1, (1.0, 1.0))
        with self.assertRaises(ValueError):
            StarSystem("Beta", "Red dwarf", "Single", 1, (2.0, 1.0))

    def test_is_habitable_false_cases(self):
        s_none = StarSystem("A", "Red dwarf", "Single", 3, None)
        self.assertFalse(s_none.is_habitable)

        s_zero_planets = StarSystem("B", "Red dwarf", "Single", 0, (0.5, 1.0))
        self.assertFalse(s_zero_planets.is_habitable)

    def test_gt_comparison_wider_and_equal(self):
        s1 = StarSystem("Wide", "Yellow dwarf", "Single", 1, (0.5, 3.0))
        s2 = StarSystem("Narrow", "Yellow dwarf", "Single", 1, (1.0, 2.0))
        self.assertTrue(s1 > s2)

        s3 = StarSystem("EqualA", "Yellow dwarf", "Single", 1, (1.0, 2.0))
        s4 = StarSystem("EqualB", "Yellow dwarf", "Single", 1, (2.0, 3.0))
        # both ranges length 1.0 -> s3 > s4 should be False
        self.assertFalse(s3 > s4)

    def test_gt_raises_if_not_habitable(self):
        hab = StarSystem("Hab", "Yellow dwarf", "Single", 1, (1.0, 2.0))
        not_hab = StarSystem("Nope", "Yellow dwarf", "Single", 0, None)
        with self.assertRaises(ValueError):
            _ = hab > not_hab
        with self.assertRaises(ValueError):
            _ = not_hab > hab

    def test_compare_star_systems_messages(self):
        s1 = StarSystem("S1", "Yellow dwarf", "Single", 1, (0.5, 2.5))
        s2 = StarSystem("S2", "Yellow dwarf", "Single", 1, (1.0, 2.0))
        msg = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual(msg, "S1 has a wider habitable zone than S2.")

        msg2 = StarSystem.compare_star_systems(s2, s1)
        self.assertEqual(msg2, "S1 has a wider or equal habitable zone compared to S2.")

        # When comparison not possible it should return the error message
        s_no = StarSystem("No", "Red dwarf", "Single", 0, None)
        result = StarSystem.compare_star_systems(s1, s_no)
        self.assertIn("Comparison not possible", result)


if __name__ == "__main__":
    unittest.main()

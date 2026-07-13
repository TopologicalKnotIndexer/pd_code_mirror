from copy import deepcopy
import unittest

from pd_code_mirror import mirror_pd_code


TREFOIL = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]


class MirrorTests(unittest.TestCase):
    def test_mirror_is_an_involution_without_mutation(self):
        source = deepcopy(TREFOIL)
        mirrored = mirror_pd_code(source)
        self.assertEqual(mirror_pd_code(mirrored), TREFOIL)
        self.assertEqual(source, TREFOIL)

    def test_accepts_empty_unknot_and_rejects_invalid_code(self):
        self.assertEqual(mirror_pd_code([]), [])
        with self.assertRaises(TypeError):
            mirror_pd_code([[1, 2, 3, 4]])


if __name__ == "__main__":
    unittest.main()

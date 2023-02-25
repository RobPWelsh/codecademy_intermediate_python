import unittest
import surfshop


class SurfShopTests(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_one_surfboard(self):
        add_one_surfboard = self.cart.add_surfboards(1)
        self.assertEqual(add_one_surfboard, 'Successfully added 1 surfboard to cart!')

    def test_add_more_surfboards(self):
        quantities = [2, 3, 4]
        for qty in quantities:
            with self.subTest(qty):
                add_more_surfboards = self.cart.add_surfboards(qty)
                self.assertEqual(add_more_surfboards, 'Successfully added ' + str(qty) + ' surfboards to cart!')
                self.cart = surfshop.ShoppingCart()  # creates a new instance and sets num_surfboards to 0

    # @unittest.skip
    def test_add_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
        print()

    # @unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.apply_locals_discount)


if __name__ == '__main__':
    unittest.main()


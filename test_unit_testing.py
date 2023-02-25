import unittest
import entertainment
import alerts
# import entertainment_2
# import kiosk
# import entertainment_3
# import feedback


# Using Assert
# destinations = {
#     'BUD': 'Budapest',
#     'CMN': 'Casablanca',
#     'IST': 'Istanbul'
# }
# print('Welcome to Small World Airlines!')
# print('What is the airport code of your travel destination?')
# destination = 'HND'
#
# # Write your code below:
# assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'
#
# city_name = destinations[destination]
# print('Great! Retrieving information for your flight to ...' + city_name)

# _____________________________________________________________________________
# Unit Testing
# def get_nearest_exit(row_number):
#     if row_number < 15:
#         location = 'front'
#     elif row_number < 30:
#         location = 'middle'
#     else:
#         location = 'back'
#     return location
#
#
# # Write your code below:
# class NearestExitTests(unittest.TestCase):
#     def test_row_1(self):
#         self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
#
#     def test_row_20(self):
#         self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
#
#     def test_row_40(self):
#         self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')


# ____________________________________________________________________________________________________
# Equality, Membership, Quantitative Methods

# class EntertainmentSystemTests(unittest.TestCase):
#
#     def test_movie_license(self):
#         daily_movie = entertainment.get_daily_movie()
#         licensed_movies = entertainment.get_licensed_movies()
#         self.assertIn(daily_movie, licensed_movies)
#
#     def test_wifi_status(self):
#         wifi_enabled = entertainment.get_wifi_status()
#         self.assertTrue(wifi_enabled, 'WiFi is inactive')
#
#     def test_maximum_display_brightness(self):
#         brightness = entertainment.get_maximum_display_brightness()
#         self.assertAlmostEqual(brightness, 400)
#
#     def test_device_temperature(self):
#         device_temp = entertainment.get_device_temp()
#         self.assertLess(device_temp, 45)


# ____________________________________________________________________________________________________
# Exception and Warning Methods

class SystemAlertTests(unittest.TestCase):
    def test_power_outage_alert(self):
        self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)

    def test_water_levels_warning(self):
        self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)


# ____________________________________________________________________________________________________
# Parameterizing Tests
# class EntertainmentSystemTests(unittest.TestCase):
#
#     def test_movie_license(self):
#         daily_movies = entertainment_2.get_daily_movies()
#         licensed_movies = entertainment_2.get_licensed_movies()
#
#         # Write your code below:
#         for movie in daily_movies:
#             print(movie)
#             with self.subTest(movie):
#                 self.assertIn(movie, licensed_movies)
# ____________________________________________________________________________________________________
# Test Fixtures
# class CheckInKioskTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         kiosk.power_on_kiosk()
#
#     def setUp(self):
#         kiosk.return_to_welcome_page()
#
#     def test_check_in_with_flight_number(self):
#         print('Testing the check-in process based on flight number')
#
#     def test_check_in_with_passport(self):
#         print('Testing the check-in process based on passport')
#
#     @classmethod
#     def tearDownClass(cls):
#         kiosk.power_off_kiosk()

# ____________________________________________________________________________________________________
# Skipping Tests
# class EntertainmentSystemTests(unittest.TestCase):
#
#     @unittest.skipIf(entertainment_3.regional_jet(), 'Not available on regional jets')
#     def test_movie_license(self):
#         daily_movie = entertainment_3.get_daily_movie()
#         licensed_movies = entertainment_3.get_licensed_movies()
#         self.assertIn(daily_movie, licensed_movies)
#
#     @unittest.skipUnless(not entertainment_3.regional_jet(), 'Not available on regional jets')
#     def test_wifi_status(self):
#         wifi_enabled = entertainment_3.get_wifi_status()
#         self.assertTrue(wifi_enabled)
#
#     def test_device_temperature(self):
#         if entertainment_3.regional_jet():
#             self.skipTest('Not available on regional jets')
#         device_temp = entertainment_3.get_device_temp()
#         self.assertLess(device_temp, 35)
#
#     def test_maximum_display_brightness(self):
#         if entertainment_3.regional_jet():
#             self.skipTest('Not available on regional jets')
#         brightness = entertainment_3.get_maximum_display_brightness()
#         self.assertAlmostEqual(brightness, 400)

# ____________________________________________________________________________________________________
# Expected failures
# class CustomerFeedbackTests(unittest.TestCase):
#
#   # Write your code below:
#
#   @unittest.expectedFailure
#   def test_survey_form(self):
#     self.assertEqual(feedback.issue_survey(), 'Success')
#
#   def test_complaint_form(self):
#     self.assertEqual(feedback.log_customer_complaint(), 'Success')
#
#
if __name__ == '__main__':
    unittest.main()

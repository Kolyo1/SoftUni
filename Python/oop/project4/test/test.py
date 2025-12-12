import unittest
from restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    """Test cases for the Restaurant class"""
    
    # ===== Initialization Tests =====
    
    def test_restaurant_initialized_with_valid_name_and_capacity(self):
        """Test that restaurant is initialized correctly with valid parameters"""
        restaurant = Restaurant("Test Restaurant", 10)
        self.assertEqual(restaurant.name, "Test Restaurant")
        self.assertEqual(restaurant.capacity, 10)
        self.assertEqual(restaurant.waiters, [])

    def test_restaurant_name_setter_with_empty_string(self):
        """Test that empty string raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Restaurant("", 10)
        self.assertEqual(str(context.exception), "Invalid name!")

    def test_restaurant_name_setter_with_only_spaces(self):
        """Test that string with only spaces raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Restaurant("   ", 10)
        self.assertEqual(str(context.exception), "Invalid name!")

    def test_restaurant_name_setter_with_none(self):
        """Test that None name raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Restaurant(None, 10)
        self.assertEqual(str(context.exception), "Invalid name!")

    def test_restaurant_capacity_setter_with_negative_value(self):
        """Test that negative capacity raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Restaurant("Test Restaurant", -5)
        self.assertEqual(str(context.exception), "Invalid capacity!")

    def test_restaurant_capacity_setter_with_zero(self):
        """Test that zero capacity is valid"""
        restaurant = Restaurant("Test Restaurant", 0)
        self.assertEqual(restaurant.capacity, 0)

    def test_restaurant_capacity_setter_with_positive_value(self):
        """Test that positive capacity is valid"""
        restaurant = Restaurant("Test Restaurant", 100)
        self.assertEqual(restaurant.capacity, 100)

    def test_restaurant_initialization_with_minimal_valid_data(self):
        """Test initialization with minimal valid data"""
        restaurant = Restaurant("A", 0)
        self.assertEqual(restaurant.name, "A")
        self.assertEqual(restaurant.capacity, 0)

    def test_name_property_getter(self):
        """Test that name property getter works correctly"""
        restaurant = Restaurant("My Restaurant", 20)
        self.assertEqual(restaurant.name, "My Restaurant")

    def test_capacity_property_getter(self):
        """Test that capacity property getter works correctly"""
        restaurant = Restaurant("My Restaurant", 30)
        self.assertEqual(restaurant.capacity, 30)

    def test_initial_waiters_list_is_empty(self):
        """Test that waiters list is initially empty"""
        restaurant = Restaurant("Test", 5)
        self.assertEqual(len(restaurant.waiters), 0)
        self.assertEqual(restaurant.waiters, [])
    
    # ===== Add Waiter Tests =====
    
    def test_add_waiter_successfully(self):
        """Test adding a waiter successfully"""
        restaurant = Restaurant("Test Restaurant", 3)
        result = restaurant.add_waiter("John")
        self.assertEqual(result, "The waiter John has been added.")
        self.assertEqual(len(restaurant.waiters), 1)
        self.assertEqual(restaurant.waiters[0]['name'], "John")

    def test_add_multiple_waiters_successfully(self):
        """Test adding multiple waiters successfully"""
        restaurant = Restaurant("Test Restaurant", 3)
        results = [
            restaurant.add_waiter("John"),
            restaurant.add_waiter("Alice"),
            restaurant.add_waiter("Bob")
        ]
        
        expected_results = [
            "The waiter John has been added.",
            "The waiter Alice has been added.",
            "The waiter Bob has been added."
        ]
        
        self.assertEqual(results, expected_results)
        self.assertEqual(len(restaurant.waiters), 3)

    def test_add_duplicate_waiter(self):
        """Test adding a waiter with the same name"""
        restaurant = Restaurant("Test Restaurant", 3)
        restaurant.add_waiter("John")
        result = restaurant.add_waiter("John")
        self.assertEqual(result, "The waiter John already exists!")
        self.assertEqual(len(restaurant.waiters), 1)

    def test_add_waiter_when_at_capacity(self):
        """Test adding waiter when restaurant is at capacity"""
        restaurant = Restaurant("Test Restaurant", 2)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        
        # Try to add one more
        result = restaurant.add_waiter("Bob")
        self.assertEqual(result, "No more places!")
        self.assertEqual(len(restaurant.waiters), 2)

    def test_add_waiter_with_special_characters_in_name(self):
        """Test adding waiter with special characters in name"""
        restaurant = Restaurant("Test Restaurant", 3)
        result = restaurant.add_waiter("John-Doe")
        self.assertEqual(result, "The waiter John-Doe has been added.")
        self.assertEqual(restaurant.waiters[0]['name'], "John-Doe")

    def test_add_waiter_with_spaces_in_name(self):
        """Test adding waiter with spaces in name"""
        restaurant = Restaurant("Test Restaurant", 3)
        result = restaurant.add_waiter("John Smith")
        self.assertEqual(result, "The waiter John Smith has been added.")
        self.assertEqual(restaurant.waiters[0]['name'], "John Smith")

    def test_add_waiter_with_empty_string_name(self):
        """Test adding waiter with empty string name"""
        restaurant = Restaurant("Test Restaurant", 3)
        result = restaurant.add_waiter("")
        self.assertEqual(result, "The waiter  has been added.")
        self.assertEqual(restaurant.waiters[0]['name'], "")

    def test_add_waiter_case_sensitivity(self):
        """Test that waiter names are case-sensitive"""
        restaurant = Restaurant("Test Restaurant", 3)
        restaurant.add_waiter("john")
        result = restaurant.add_waiter("John")
        self.assertEqual(result, "The waiter John has been added.")
        self.assertEqual(len(restaurant.waiters), 2)

    def test_waiter_structure(self):
        """Test the structure of waiter dictionary"""
        restaurant = Restaurant("Test Restaurant", 3)
        restaurant.add_waiter("John")
        waiter = restaurant.waiters[0]
        self.assertIsInstance(waiter, dict)
        self.assertEqual(waiter['name'], "John")
        self.assertTrue('name' in waiter)
    
    # ===== Remove Waiter Tests =====
    
    def test_remove_existing_waiter(self):
        """Test removing an existing waiter"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.add_waiter("Bob")
        restaurant.add_waiter("Charlie")
        
        initial_count = len(restaurant.waiters)
        result = restaurant.remove_waiter("Alice")
        
        self.assertEqual(result, "The waiter Alice has been removed.")
        self.assertEqual(len(restaurant.waiters), initial_count - 1)
        
        # Check that Alice is not in the list
        waiter_names = [waiter['name'] for waiter in restaurant.waiters]
        self.assertNotIn("Alice", waiter_names)

    def test_remove_first_waiter(self):
        """Test removing the first waiter in the list"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.add_waiter("Bob")
        
        result = restaurant.remove_waiter("John")
        self.assertEqual(result, "The waiter John has been removed.")
        
        waiter_names = [waiter['name'] for waiter in restaurant.waiters]
        self.assertNotIn("John", waiter_names)
        self.assertIn("Alice", waiter_names)

    def test_remove_last_waiter(self):
        """Test removing the last waiter in the list"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.add_waiter("Bob")
        
        result = restaurant.remove_waiter("Bob")
        self.assertEqual(result, "The waiter Bob has been removed.")
        
        waiter_names = [waiter['name'] for waiter in restaurant.waiters]
        self.assertNotIn("Bob", waiter_names)
        self.assertIn("Alice", waiter_names)

    def test_remove_non_existing_waiter(self):
        """Test removing a waiter that doesn't exist"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.add_waiter("Bob")
        
        initial_count = len(restaurant.waiters)
        result = restaurant.remove_waiter("David")
        
        self.assertEqual(result, "No waiter found with the name David.")
        self.assertEqual(len(restaurant.waiters), initial_count)

    def test_remove_waiter_case_sensitivity(self):
        """Test that waiter removal is case-sensitive"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.add_waiter("Bob")
        
        initial_count = len(restaurant.waiters)
        result = restaurant.remove_waiter("john")  # lowercase
        
        self.assertEqual(result, "No waiter found with the name john.")
        self.assertEqual(len(restaurant.waiters), initial_count)

    def test_remove_waiter_with_empty_string(self):
        """Test removing waiter with empty string name"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        
        initial_count = len(restaurant.waiters)
        result = restaurant.remove_waiter("")
        
        self.assertEqual(result, "No waiter found with the name .")
        self.assertEqual(len(restaurant.waiters), initial_count)

    def test_remove_all_waiters(self):
        """Test removing all waiters one by one"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.add_waiter("Bob")
        restaurant.add_waiter("Charlie")
        
        waiters_to_remove = ["John", "Alice", "Bob", "Charlie"]
        
        for waiter_name in waiters_to_remove:
            result = restaurant.remove_waiter(waiter_name)
            self.assertEqual(result, f"The waiter {waiter_name} has been removed.")
        
        self.assertEqual(len(restaurant.waiters), 0)

    def test_remove_waiter_and_then_add_again(self):
        """Test removing a waiter and then adding them again"""
        restaurant = Restaurant("Test Restaurant", 5)
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        restaurant.add_waiter("Bob")
        
        # Remove Alice
        restaurant.remove_waiter("Alice")
        
        # Try to add Alice again
        result = restaurant.add_waiter("Alice")
        self.assertEqual(result, "The waiter Alice has been added.")
        self.assertEqual(len(restaurant.waiters), 3)
    
    # ===== Get Waiters Tests =====
    
    def test_get_all_waiters_no_filters(self):
        """Test getting all waiters without filters"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters()
        self.assertEqual(len(result), 5)
        self.assertEqual(result, restaurant.waiters)

    def test_get_waiters_with_min_earnings(self):
        """Test filtering waiters by minimum earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(min_earnings=150)
        self.assertEqual(len(result), 3)
        
        # Check that all returned waiters have earnings >= 150
        for waiter in result:
            self.assertGreaterEqual(waiter['total_earnings'], 150)

    def test_get_waiters_with_max_earnings(self):
        """Test filtering waiters by maximum earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(max_earnings=150)
        self.assertEqual(len(result), 3)
        
        # Check that all returned waiters have earnings <= 150
        for waiter in result:
            self.assertLessEqual(waiter['total_earnings'], 150)

    def test_get_waiters_with_min_and_max_earnings(self):
        """Test filtering waiters by both min and max earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(min_earnings=100, max_earnings=200)
        self.assertEqual(len(result), 3)
        
        # Check that all returned waiters have earnings between 100 and 200
        for waiter in result:
            self.assertGreaterEqual(waiter['total_earnings'], 100)
            self.assertLessEqual(waiter['total_earnings'], 200)

    def test_get_waiters_with_exact_min_earnings(self):
        """Test filtering with min earnings equal to a waiter's earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(min_earnings=150)
        self.assertEqual(len(result), 3)
        
        # Should include Bob who has exactly 150
        waiter_names = [waiter['name'] for waiter in result]
        self.assertIn('Bob', waiter_names)

    def test_get_waiters_with_exact_max_earnings(self):
        """Test filtering with max earnings equal to a waiter's earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(max_earnings=150)
        self.assertEqual(len(result), 3)
        
        # Should include Bob who has exactly 150
        waiter_names = [waiter['name'] for waiter in result]
        self.assertIn('Bob', waiter_names)

    def test_get_waiters_with_no_matches(self):
        """Test filtering when no waiters match the criteria"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(min_earnings=1000)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_get_waiters_with_waiter_having_no_earnings_key(self):
        """Test when some waiters don't have 'total_earnings' key"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        # Add a waiter without total_earnings
        restaurant.waiters.append({'name': 'Eve'})
        
        result = restaurant.get_waiters(min_earnings=100)
        # Eve should not be included since she has no earnings (treated as 0)
        # Waiters with earnings >= 100: John(100), Alice(200), Bob(150), Charlie(300)
        self.assertEqual(len(result), 4)
        
        # Check that Eve is not in the results
        waiter_names = [waiter['name'] for waiter in result]
        self.assertNotIn('Eve', waiter_names)
        
        # Check that all included waiters have earnings >= 100
        for waiter in result:
            self.assertGreaterEqual(waiter.get('total_earnings', 0), 100)

    def test_get_waiters_with_all_waiters_having_no_earnings(self):
        """Test filtering when no waiters have earnings data"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John'},
            {'name': 'Alice'},
            {'name': 'Bob'}
        ]
        
        result = restaurant.get_waiters(min_earnings=100)
        self.assertEqual(len(result), 0)

    def test_get_waiters_with_zero_min_earnings(self):
        """Test filtering with min_earnings=0"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(min_earnings=0)
        self.assertEqual(len(result), 5)

    def test_get_waiters_with_zero_max_earnings(self):
        """Test filtering with max_earnings=0"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(max_earnings=0)
        # Only waiters with earnings <= 0 or no earnings
        self.assertEqual(len(result), 0)  # All our waiters have positive earnings

    def test_get_waiters_with_negative_min_earnings(self):
        """Test filtering with negative min_earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(min_earnings=-100)
        self.assertEqual(len(result), 5)  # All waiters should be included

    def test_get_waiters_with_negative_max_earnings(self):
        """Test filtering with negative max_earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150},
            {'name': 'Charlie', 'total_earnings': 300},
            {'name': 'David', 'total_earnings': 50}
        ]
        
        result = restaurant.get_waiters(max_earnings=-100)
        self.assertEqual(len(result), 0)  # No waiters have negative earnings
    
    # ===== Get Total Earnings Tests =====
    
    def test_total_earnings_with_no_waiters(self):
        """Test total earnings when there are no waiters"""
        restaurant = Restaurant("Test Restaurant", 10)
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 0)

    def test_total_earnings_with_waiters_having_earnings(self):
        """Test total earnings calculation with multiple waiters"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150}
        ]
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 450)  # 100 + 200 + 150

    def test_total_earnings_with_waiter_having_no_earnings_key(self):
        """Test total earnings when some waiters don't have earnings key"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice'},  # No total_earnings key
            {'name': 'Bob', 'total_earnings': 150}
        ]
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 250)  # 100 + 0 + 150

    def test_total_earnings_with_zero_earnings(self):
        """Test total earnings when all waiters have zero earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 0},
            {'name': 'Alice', 'total_earnings': 0},
            {'name': 'Bob', 'total_earnings': 0}
        ]
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 0)

    def test_total_earnings_with_negative_earnings(self):
        """Test total earnings when some waiters have negative earnings"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': -50},
            {'name': 'Bob', 'total_earnings': 150}
        ]
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 200)  # 100 + (-50) + 150

    def test_total_earnings_with_float_earnings(self):
        """Test total earnings with floating point values"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100.50},
            {'name': 'Alice', 'total_earnings': 200.75},
            {'name': 'Bob', 'total_earnings': 150.25}
        ]
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 451.50)  # 100.50 + 200.75 + 150.25

    def test_total_earnings_with_mixed_types(self):
        """Test total earnings with different numeric types"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},    # int
            {'name': 'Alice', 'total_earnings': 200.5}, # float
            {'name': 'Bob', 'total_earnings': 0}        # int
        ]
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 300.5)

    def test_total_earnings_after_adding_waiters(self):
        """Test total earnings after dynamically adding waiters"""
        restaurant = Restaurant("Test Restaurant", 10)
        # Add waiters
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        
        # Manually set earnings (since add_waiter doesn't set earnings)
        restaurant.waiters[0]['total_earnings'] = 100
        restaurant.waiters[1]['total_earnings'] = 200
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 300)

    def test_total_earnings_after_removing_waiters(self):
        """Test total earnings after removing a waiter"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 200},
            {'name': 'Bob', 'total_earnings': 150}
        ]
        
        # Remove Alice
        restaurant.remove_waiter("Alice")
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 250)  # 100 + 150

    def test_total_earnings_with_large_numbers(self):
        """Test total earnings with very large numbers"""
        restaurant = Restaurant("Test Restaurant", 10)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 1000000},
            {'name': 'Alice', 'total_earnings': 2000000},
            {'name': 'Bob', 'total_earnings': 1500000}
        ]
        
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 4500000)
    
    # ===== Integration Tests =====
    
    def test_complete_restaurant_workflow(self):
        """Test a complete workflow of restaurant operations"""
        # 1. Initialize restaurant
        restaurant = Restaurant("Fine Dining", 4)
        self.assertEqual(restaurant.name, "Fine Dining")
        self.assertEqual(restaurant.capacity, 4)
        
        # 2. Add waiters
        results = []
        results.append(restaurant.add_waiter("John"))
        results.append(restaurant.add_waiter("Alice"))
        results.append(restaurant.add_waiter("Bob"))
        
        expected_add_results = [
            "The waiter John has been added.",
            "The waiter Alice has been added.",
            "The waiter Bob has been added."
        ]
        self.assertEqual(results, expected_add_results)
        self.assertEqual(len(restaurant.waiters), 3)
        
        # 3. Try to add duplicate waiter
        duplicate_result = restaurant.add_waiter("John")
        self.assertEqual(duplicate_result, "The waiter John already exists!")
        self.assertEqual(len(restaurant.waiters), 3)
        
        # 4. Try to add Charlie - should work (4th waiter with capacity 4)
        charlie_result = restaurant.add_waiter("Charlie")
        self.assertEqual(charlie_result, "The waiter Charlie has been added.")
        self.assertEqual(len(restaurant.waiters), 4)
        
        # 5. Try to add waiter beyond capacity (5th waiter)
        beyond_capacity_result = restaurant.add_waiter("David")
        self.assertEqual(beyond_capacity_result, "No more places!")
        self.assertEqual(len(restaurant.waiters), 4)
        
        # 6. Set earnings for waiters
        restaurant.waiters[0]['total_earnings'] = 100  # John
        restaurant.waiters[1]['total_earnings'] = 200  # Alice
        restaurant.waiters[2]['total_earnings'] = 150  # Bob
        restaurant.waiters[3]['total_earnings'] = 300  # Charlie
        
        # 7. Test get_waiters with filters
        filtered = restaurant.get_waiters(min_earnings=150)
        self.assertEqual(len(filtered), 3)  # Alice(200), Bob(150), Charlie(300)
        
        # 8. Test total earnings
        total = restaurant.get_total_earnings()
        self.assertEqual(total, 750)  # 100 + 200 + 150 + 300
        
        # 9. Remove a waiter
        remove_result = restaurant.remove_waiter("Alice")
        self.assertEqual(remove_result, "The waiter Alice has been removed.")
        self.assertEqual(len(restaurant.waiters), 3)
        
        # 10. Check total earnings after removal
        total_after_removal = restaurant.get_total_earnings()
        self.assertEqual(total_after_removal, 550)  # 100 + 150 + 300
        
        # 11. Add a new waiter after removal
        new_waiter_result = restaurant.add_waiter("Eve")
        self.assertEqual(new_waiter_result, "The waiter Eve has been added.")
        self.assertEqual(len(restaurant.waiters), 4)
        
        # 12. Set earnings for new waiter
        for waiter in restaurant.waiters:
            if waiter['name'] == 'Eve':
                waiter['total_earnings'] = 250
        
        # 13. Final total earnings
        final_total = restaurant.get_total_earnings()
        # John(100) + Bob(150) + Charlie(300) + Eve(250) = 800
        self.assertEqual(final_total, 800)

    def test_edge_cases_integration(self):
        """Test edge cases in an integrated manner"""
        # Restaurant with capacity 0
        restaurant = Restaurant("Empty Restaurant", 0)
        
        # Try to add waiter to restaurant with capacity 0
        result = restaurant.add_waiter("John")
        self.assertEqual(result, "No more places!")
        self.assertEqual(len(restaurant.waiters), 0)
        
        # Remove non-existent waiter
        remove_result = restaurant.remove_waiter("Ghost")
        self.assertEqual(remove_result, "No waiter found with the name Ghost.")
        
        # Get waiters with filters on empty list
        filtered = restaurant.get_waiters(min_earnings=100)
        self.assertEqual(filtered, [])
        
        # Get total earnings on empty list
        total = restaurant.get_total_earnings()
        self.assertEqual(total, 0)

    def test_name_and_capacity_changes_integration(self):
        """Test that name and capacity changes don't affect waiters"""
        restaurant = Restaurant("Original Name", 3)
        
        # Add some waiters
        restaurant.add_waiter("John")
        restaurant.add_waiter("Alice")
        
        # Change name through reinitialization (not typical, but testing)
        # Note: In real code, you wouldn't reinitialize, but properties ensure data integrity
        self.assertEqual(restaurant.name, "Original Name")
        
        # Test capacity constraint still works
        restaurant.add_waiter("Bob")  # 3rd waiter
        result = restaurant.add_waiter("Charlie")  # Should fail
        self.assertEqual(result, "No more places!")
        
        # Remove a waiter and add new one
        restaurant.remove_waiter("Alice")
        result = restaurant.add_waiter("David")
        self.assertEqual(result, "The waiter David has been added.")


if __name__ == '__main__':
    unittest.main()
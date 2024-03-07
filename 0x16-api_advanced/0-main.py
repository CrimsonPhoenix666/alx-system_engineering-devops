#!/usr/bin/python3
"""
Test script for the number_of_subscribers function.
"""

if __name__ == "__main__":
    from subs import number_of_subscribers

    # Test with an existing subreddit
    existing_subreddit = "programming"
    result_existing = number_of_subscribers(existing_subreddit)
    expected_existing = 756024
    print(f"Subscribers for {existing_subreddit}: {result_existing}")
    print(f"Expected subscribers: {expected_existing}")
    print(f"Result matches expected: {result_existing == expected_existing}")

    # Test with a non-existing subreddit
    non_existing_subreddit = "this_is_a_fake_subreddit"
    result_non_existing = number_of_subscribers(non_existing_subreddit)
    expected_non_existing = 0
    print(f"Subscribers for {non_existing_subreddit}: {result_non_existing}")
    print(f"Expected subscribers: {expected_non_existing}")
    print(f"Result matches expected: {result_non_existing == expected_non_existing}")

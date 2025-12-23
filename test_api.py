import requests
import json
import uuid

BASE_URL = "http://localhost:8000"

def test_person_api():
    print("Testing Person API...")
    # Create
    person_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "birth_date": "1990-01-01"
    }
    response = requests.post(f"{BASE_URL}/persons/", data=person_data)
    if response.status_code != 201:
        print(f"Failed to create person: {response.status_code} {response.text}")
        return None
    person_id = response.json()['id']
    print(f"Created person with ID: {person_id}")

    # List and Search
    response = requests.get(f"{BASE_URL}/persons/?search=John")
    if len(response.json()['results']) == 0:
        print("Search failed for Person")
    else:
        print("Search successful for Person")

    return person_id

def test_group_api():
    print("\nTesting Group API...")
    # Create
    group_data = {
        "name": "Developers"
    }
    response = requests.post(f"{BASE_URL}/auth-groups/", data=group_data)
    if response.status_code != 201:
        print(f"Failed to create group: {response.status_code} {response.text}")
        return None
    group_id = response.json()['id']
    print(f"Created group with ID: {group_id}")

    # List and Search
    response = requests.get(f"{BASE_URL}/auth-groups/?search=Developers")
    if len(response.json()['results']) == 0:
        print("Search failed for Group")
    else:
        print("Search successful for Group")

    return group_id

def test_membership_api(person_id, group_id):
    print("\nTesting Membership API...")
    if not person_id or not group_id:
        print("Skipping Membership test due to missing person or group ID")
        return

    # Create
    membership_data = {
        "person": person_id,
        "group": group_id,
        "date_joined": "2023-01-01"
    }
    response = requests.post(f"{BASE_URL}/memberships/", data=membership_data)
    if response.status_code != 201:
        print(f"Failed to create membership: {response.status_code} {response.text}")
        return

    print("Created membership")

    # List and Search
    response = requests.get(f"{BASE_URL}/memberships/?search=Developers")
    if len(response.json()['results']) == 0:
        print("Search failed for Membership")
    else:
        print("Search successful for Membership")

if __name__ == "__main__":
    try:
        # Check if server is up
        try:
            requests.get(BASE_URL)
        except requests.exceptions.ConnectionError:
            print("Server is not running. Please start the server first.")
            exit(1)

        person_id = test_person_api()
        group_id = test_group_api()
        test_membership_api(person_id, group_id)
        
    except Exception as e:
        print(f"An error occurred: {e}")

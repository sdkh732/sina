import json
import os

class PatientDataManager:
    def __init__(self, data_file_path="patient_data.json"):
        self.data_file_path = data_file_path
        self.patient_data = {}
        self.load_data()

    def add_patient_record(self, patient_id, patient_name, scan_data_reference):
        """Adds a new patient record."""
        if patient_id in self.patient_data:
            print(f"Warning: Patient ID {patient_id} already exists. Overwriting.")
        self.patient_data[patient_id] = {
            "name": patient_name,
            "scan_data_reference": scan_data_reference
        }
        print(f"Record added for patient ID {patient_id}.")

    def get_patient_record(self, patient_id):
        """Retrieves a patient record by patient_id."""
        return self.patient_data.get(patient_id, None)

    def save_data(self):
        """Saves the current patient data to the JSON file."""
        try:
            with open(self.data_file_path, 'w') as f:
                json.dump(self.patient_data, f, indent=4)
            print(f"Data saved to {self.data_file_path}")
        except IOError as e:
            print(f"Error saving data to {self.data_file_path}: {e}")

    def load_data(self):
        """Loads patient data from the JSON file if it exists."""
        if not os.path.exists(self.data_file_path):
            print(f"Data file {self.data_file_path} not found. Starting with empty data.")
            self.patient_data = {}
            return

        try:
            with open(self.data_file_path, 'r') as f:
                self.patient_data = json.load(f)
            print(f"Data loaded from {self.data_file_path}")
        except IOError as e:
            print(f"Error loading data from {self.data_file_path}: {e}. Starting with empty data.")
            self.patient_data = {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {self.data_file_path}: {e}. Starting with empty data.")
            self.patient_data = {}

if __name__ == "__main__":
    print("Starting PatientDataManager Test Suite...")
    test_file = "test_patient_data.json"

    # Clean up before test, if file exists from a previous failed run
    if os.path.exists(test_file):
        os.remove(test_file)

    # 1. Create an instance of PatientDataManager
    print("\nStep 1: Creating first PatientDataManager instance...")
    manager1 = PatientDataManager(data_file_path=test_file)

    # 2. Add a few patient records
    print("\nStep 2: Adding patient records...")
    manager1.add_patient_record("P001", "John Doe", "scan_ref_001.stl")
    manager1.add_patient_record("P002", "Jane Smith", "scan_ref_002.stl")
    manager1.add_patient_record("P003", "Alice Brown", "/path/to/scan_003.npy")

    # Verify records in manager1
    print("\nVerifying records in manager1:")
    print("Record P001:", manager1.get_patient_record("P001"))
    print("Record P002:", manager1.get_patient_record("P002"))

    # 3. Save the data
    print("\nStep 3: Saving data...")
    manager1.save_data()

    # 4. Create another instance of PatientDataManager (simulating loading from the file)
    print("\nStep 4: Creating second PatientDataManager instance to load data...")
    manager2 = PatientDataManager(data_file_path=test_file)

    # 5. Retrieve and print the records to verify they were saved and loaded correctly
    print("\nStep 5: Retrieving and verifying records from manager2...")
    record_p001_loaded = manager2.get_patient_record("P001")
    record_p002_loaded = manager2.get_patient_record("P002")
    record_p003_loaded = manager2.get_patient_record("P003")

    print("Loaded Record P001:", record_p001_loaded)
    print("Loaded Record P002:", record_p002_loaded)
    print("Loaded Record P003:", record_p003_loaded)

    assert record_p001_loaded is not None and record_p001_loaded["name"] == "John Doe"
    assert record_p002_loaded is not None and record_p002_loaded["scan_data_reference"] == "scan_ref_002.stl"
    assert record_p003_loaded is not None and record_p003_loaded["name"] == "Alice Brown"

    # Test getting a non-existent record
    print("\nTesting retrieval of a non-existent record (P004):")
    non_existent_record = manager2.get_patient_record("P004")
    print("Record P004:", non_existent_record)
    assert non_existent_record is None

    # 6. Clean up by removing the test_patient_data.json file
    print("\nStep 6: Cleaning up test file...")
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"Removed test file: {test_file}")
    else:
        print(f"Test file {test_file} not found for cleanup.")

    print("\nPatientDataManager Test Suite Completed Successfully!")

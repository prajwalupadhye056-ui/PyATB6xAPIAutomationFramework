# HTTP status code
#Headers
#Data Verification
#JSON Schema


def verify_status_code(response_data_status, expected_data):
     assert response_data_status == expected_data, "Failed to Match the Status code"

def verify_response_key(key,expected_data):
    assert key == expected_data

def verify_json_key_not_null(key):
    assert key !=0, "Failed - key is non empty" + key
    assert key > 0, "Failed - Key is greater than zero"

def verify_json_key_for_not_null_token(key):
    assert key != 0,"Failed -Key is non empty" + key

def verify_response_delete(response):
    assert "Created" in response



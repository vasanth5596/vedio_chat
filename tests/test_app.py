import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home_page():
    """Test if the home page (/) loads successfully"""
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_calculate_addition():
    """Test the /calculate endpoint for addition"""
    tester = app.test_client()
    response = tester.post('/calculate',
        data=json.dumps({"num1": 10, "num2": 5, "operator": "+"}),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert response.get_json()['result'] == 15

def test_calculate_divide_by_zero():
    """Test divide by zero error"""
    tester = app.test_client()
    response = tester.post('/calculate',
        data=json.dumps({"num1": 10, "num2": 0, "operator": "/"}),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert 'Division by zero' in response.get_json()['error']

def test_invalid_operator():
    """Test invalid operator handling"""
    tester = app.test_client()
    response = tester.post('/calculate',
        data=json.dumps({"num1": 1, "num2": 2, "operator": "%"}),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert 'Invalid operator' in response.get_json()['error']

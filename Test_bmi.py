import sys
import os

# Add Lab2 folder to the system path
sys.path.insert(0, os.path.abspath('../Lab2'))

# Import the BMI module (assuming it's named Lab2.py)
import Lab2 as bmi

def test_bmi_under_weight():
    result = bmi.calculate_bmi(weight=45, height=1.75)  # BMI ≈ 14.7
    assert result == -1

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(weight=68, height=1.75)  # BMI ≈ 22.2
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(weight=85, height=1.75)  # BMI ≈ 27.8
    assert result == 1

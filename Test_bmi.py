import lab2.bmi as bmi

def test_bmi_normal_weight():
    # Testing a BMI within the normal weight range (18.5 <= BMI <= 25.0)
    result = bmi.calculate_bmi(1.73, 70)  # Adjust weight and height for normal BMI
    assert result == 0, "Expected 0 for Normal Weight, got {}".format(result)

def test_bmi_over_weight():
    # Testing a BMI in the overweight range (BMI > 25.0)
    result = bmi.calculate_bmi(1.73, 80)  # Adjust weight and height for overweight BMI
    assert result == 1, "Expected 1 for Over Weight, got {}".format(result)

def test_bmi_under_weight():
    # Testing a BMI in the underweight range (BMI < 18.5)
    result = bmi.calculate_bmi(1.73, 50)  # Adjust weight and height for underweight BMI
    assert result == -1, "Expected -1 for Under Weight, got {}".format(result)

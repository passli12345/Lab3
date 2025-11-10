import price_info

print("Test_price_info")

def test_total_cost_shopping():
    #Arrange

    excepted_result = 46.75

    #act
    result = price_info.total_cost_shopping()

    assert result == excepted_result


def test_cost_of_fruits():
    fruit_name = 'apple'
    quantity = 10
    expected_result = 12.0

    result = price_info.cost_of_fruit(fruit_name, quantity)

    assert result == expected_result
class DataTestBurger:
    bun_name = "WhiteBun"
    bun_price = 1.5
    ingredient_name_1 = "Tar-Tar"
    ingredient_name_2 = "salad"
    ingredient_type_1 = "SAUCE"
    ingredient_type_2 = "FILLING"
    ingredient_price_1 = 0.5
    ingredient_price_2 = 1.5
    expected_receipt = (
            "(==== WhiteBun ====)\n"
            "= sauce Tar-Tar =\n"
            "= filling salad =\n"
            "(==== WhiteBun ====)\n\n"
            "Price: 5.0"
        )

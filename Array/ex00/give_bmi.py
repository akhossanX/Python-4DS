def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Computes the BMI of a a list of heights and weights.

    Args:
            height (list[int  |  float]): List of heights in m.
            weight (list[int  |  float]): List of weights in Kg.

    Returns:
            list[int | float]: List of BMI values in kg/m^2.
    """
    try:
        return [w / h**2 for w, h in zip(weight, height)]
    except ZeroDivisionError:
        return [0]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns True for all entries superseeding the limit.

    Args:
            bmi (list[int  |  float]): List of BMI values in kg/m^2.
            limit (int): Treshold for superseed

    Returns:
            list[bool]: list of superseeds.
    """
    return list(map(lambda x: x > limit, bmi))


def main() -> None:
    """ """
    height = ['0']
    weight = [0]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()

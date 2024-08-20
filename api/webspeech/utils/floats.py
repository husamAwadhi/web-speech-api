def scale(value: float, scale: float, max: float = 100) -> float:
    """
    Scale a value between a min and max.

    Args:
        value (float): The value to scale.
        max (float): The max value.
        scale (float): The scale factor.

    Returns:
        float: The scaled value.
    """

    return (value / max) * scale if max > 0 else value

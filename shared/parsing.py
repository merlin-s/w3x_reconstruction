def f(s: str) -> float:
    return float(s.replace(" ", ""))


def i(s: str) -> float:
    return int(s.replace(" ", ""))


def char4(s: str) -> str:
    r = s.strip().replace("'", "")
    assert len(r) == 4
    return r
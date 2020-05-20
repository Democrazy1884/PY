def transform(p, screen):
    if isinstance(p, float):
        return int(p * screen)
    elif isinstance(p, int):
        return float(format(p / screen, '.6f'))


def xtransform(x, screen=1600):
    '''x坐标转换'''
    return transform(x, screen)


def ytransform(y, screen=900):
    '''y坐标转换'''
    return transform(y, screen)


_boost_ = (1335, 725)
_attack_1 = (391, 724)
_attack_2 = (932, 724)


class x:
    _value_ = 0
    boost = _boost_[_value_]
    attack1 = _attack_1[_value_]
    attack2 = _attack_2[_value_]


class y:
    _value_ = 1
    boost = _boost_[_value_]
    attack1 = _attack_1[_value_]
    attack2 = _attack_2[_value_]


if __name__ == "__main__":
    print(x.boost, y.boost)

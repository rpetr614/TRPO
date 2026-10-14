from feature_c import feature_c


def test_feature_c_returns_expected_string():
    assert feature_c() == "feature_c работает"


def test_feature_c_extra_returns_ok():
    from feature_c import feature_c_extra
    assert feature_c_extra() == "ok"

from is_greater import is_greater


def publish_result(test):
    ## decorate test function
    def result():
        value = test()
        if value[0] == value[1]:
            result = "PASS"
        else:
            result = "FAIL"
        print(f'{test.__name__}: {result}')
    return result

@publish_result
def test_true_when_greater():
    result = [is_greater(5, 4), True]
    return result

@publish_result
def test_false_when_smaller():
    result = [is_greater(4, 5), False]
    return False

@publish_result
def test_false_when_equal():
    result = [is_greater(5, 5), False]
    return result

if __name__ == "__main__":
    test_true_when_greater()
    test_false_when_smaller()
    test_false_when_equal()


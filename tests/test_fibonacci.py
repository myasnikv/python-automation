from project.fibonacci_main import generateFibonacci, fib_second, singleFibNumber


class TestFibonacci:

    def test_list(self):
        assert list(generateFibonacci(10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], \
            "Function returns wrong data"

    def testSecondList(self):
        assert fib_second(13) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], \
            "Function returns wrong data"

    def testSingleFibPositive(self):
        assert singleFibNumber(8) == 21, \
            "Function returns wrong data"

    def testSingleFibNegative(self):
        assert singleFibNumber(-8) == 0, \
            "Function returns wrong data"
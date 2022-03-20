app_root = blog
pkg_src = $(app_root)/
tests_src = $(app_root)/tests


pyclean=pyclean .
black = black $(pkg_src) $(tests_src)
flake8 = flake8 $(pkg_src) $(tests_src)
unittest_tests=python3 -m unittest discover -s . -p "*_test.py"


 .PHONY: format
format:
	$(isort)
	$(black)

.PHONY: test
test:
	$(unittest_tests)

.PHONY: clean
clean:
	$(pyclean)
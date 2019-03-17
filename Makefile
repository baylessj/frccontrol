.DEFAULT_GOAL=quick

.PHONY: all quick

quick:

	python setup.py build_ext --inplace
	rm *.so
	rm -r build/*

all:

	python setup.py build_ext --inplace --force
	rm *.so
	rm -r build/*
